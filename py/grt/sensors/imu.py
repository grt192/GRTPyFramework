"""/*----------------------------------------------------------------------------*/
/* Copyright (c) Kauai Labs 2013. All Rights Reserved.                        */
/*                                                                            */
/* Created in support of Team 2465 (Kauaibots).  Go Thunderchicken!           */
/*                                                                            */
/* Open Source Software - may be modified and shared by FRC teams. Any        */
/* modifications to this code must be accompanied by the nav6_License.txt file*/ 
/* in the root directory of the project.                                      */
/*----------------------------------------------------------------------------*/
"""



from imu_protocol import IMUProtocol

from wpilib.interfaces import PIDSource
from wpilib import SensorBase
from serial import Serial
from wpilib import Timer
import edu.wpi.first.wpilibj.livewindow.LiveWindowSendable


"""
 * The IMU class provides a simplified interface to the KauaiLabs nav6 IMU.
 * 
 * The IMU class enables access to basic connectivity and state information, 
 * as well as key orientation information (yaw, pitch, roll, compass heading).
 * 
 * Advanced capabilities of the nav6 IMU may be accessed via the IMUAdvanced 
 * class.
 * @author Scott
 */
 """
class IMU(SensorBase):

    YAW_HISTORY_LENGTH = 10
    DEFAULT_UPDATE_RATE_HZ  = 100
    DEFAULT_ACCEL_FSR_G     = 2
    DEFAULT_GYRO_FSR_DPS    = 2000
    
    serial_port = Serial()
    yaw_history[]
    next_yaw_history_index
    user_yaw_offset
    m_thread
    update_rate_hz

    volatile float yaw
    volatile float pitch
    volatile float roll
    volatile float compass_heading
    volatile int update_count = 0
    volatile int byte_count = 0
    volatile float nav6_yaw_offset_degrees
    volatile short accel_fsr_g
    volatile short gyro_fsr_dps
    volatile short flags    

    double last_update_time
    boolean stop = false
    private IMUProtocol.YPRUpdate ypr_update_data
    protected byte update_type = IMUProtocol.MSGID_YPR_UPDATE
    """
    /**
     * Constructs the IMU class, overriding the default update rate
     * with a custom rate which may be from 4 to 100, representing
     * the number of updates per second sent by the nav6 IMU.  
     * 
     * Note that increasing the update rate may increase the 
     * CPU utilization.
     * @param serial_port BufferingSerialPort object to use
     * @param update_rate_hz Custom Update Rate (Hz)
     */
     """
    def __init__(serial_port, update_rate_hz = None):
        ypr_update_data = IMUProtocol.YPRUpdate()
        if update_rate_hz:
            self.update_rate_hz = update_rate_hz
        else:
            self.update_rate_hz = DEFAULT_UPDATE_RATE_HZ
        flags = 0
        accel_fsr_g = DEFAULT_ACCEL_FSR_G
        gyro_fsr_dps = DEFAULT_GYRO_FSR_DPS
        self.serial_port = serial_port
        #yaw_history = [YAW_HISTORY_LENGTH]
        yaw = 0.0
        pitch = 0.0
        roll = 0.0
        try:
            #serial_port.reset()
        except SerialError:
            ex.printStackTrace()
        initIMU()
        m_thread = threading.Thread(target = self.run) #fix this!
        m_thread.start()       
    
   

    def initIMU(self):
        """
        // The nav6 IMU serial port configuration is 8 data bits, no parity, one stop bit. 
        // No flow control is used.
        // Conveniently, these are the defaults used by the WPILib's SerialPort class.
        //
        // In addition, the WPILib's SerialPort class also defaults to:
        //
        // Timeout period of 5 seconds
        // Termination ('\n' character)
        // Transmit immediately
        """
        self.initializeYawHistory()
        user_yaw_offset = 0

        #// set the nav6 into the desired update mode
        stream_command_buffer = [] #byte stream_command_buffer[] = new byte[256]
        packet_length = IMUProtocol.encodeStreamCommand( stream_command_buffer, update_type, update_rate_hz ) 
        try:
            self.serial_port.write(stream_command_buffer, packet_length)
        except Exception:
            ex.printStackTrace()

    def setStreamResponse(self, response):
        
        self.flags = response.flags
        self.nav6_yaw_offset_degrees = response.yaw_offset_degrees
        self.accel_fsr_g = response.accel_fsr_g
        self.gyro_fsr_dps = response.gyro_fsr_dps
        self.update_rate_hz = byte(response.update_rate_hz) #fix!
    
        
    def initializeYawHistory(self):

        self.yaw_history = []
        self.next_yaw_history_index = 0
        self.last_update_time = 0.0
    

    def setYawPitchRoll(self, yaw, pitch, roll, compass_heading):

        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll
        self.compass_heading = compass_heading

        self.updateYawHistory(self.yaw)
    

    def updateYawHistory(self, curr_yaw):

        if (self.next_yaw_history_index >= YAW_HISTORY_LENGTH) 
            self.next_yaw_history_index = 0
        
        self.yaw_history[self.next_yaw_history_index] = curr_yaw
        self.last_update_time = Timer.getFPGATimestamp()
        self.next_yaw_history_index++
    

    def getAverageFromYawHistory(self):

        yaw_history_sum = 0.0
        for i in enumerate(0, YAW_HISTORY_LENGTH):
            yaw_history_sum += self.yaw_history[i]
        
        yaw_history_avg = yaw_history_sum / YAW_HISTORY_LENGTH
        return yaw_history_avg
    

    """
    /**
     * Returns the current pitch value (in degrees, from -180 to 180)
     * reported by the nav6 IMU.
     * @return The current pitch value in degrees (-180 to 180).
     */
     """
    def getPitch(self):
        return self.pitch
    
    """
    /**
     * Returns the current roll value (in degrees, from -180 to 180)
     * reported by the nav6 IMU.
     * @return The current roll value in degrees (-180 to 180).
     */
     """
    def getRoll(self):
        return self.roll
    
    """
    /**
     * Returns the current yaw value (in degrees, from -180 to 180)
     * reported by the nav6 IMU.
     * 
     * Note that the returned yaw value will be offset by a user-specified
     * offset value this user-specified offset value is set by 
     * invoking the zeroYaw() method.
     * @return The current yaw value in degrees (-180 to 180).
     */
     """
    def getYaw(self):
        calculated_yaw = self.yaw - user_yaw_offset)
        if (calculated_yaw < -180):
            calculated_yaw += 360
        
        if (calculated_yaw > 180):
            calculated_yaw -= 360
        
        return calculated_yaw
    

    """
    /**
     * Returns the current tilt-compensated compass heading 
     * value (in degrees, from 0 to 360) reported by the nav6 IMU.
     * 
     * Note that this value is sensed by the nav6 magnetometer,
     * which can be affected by nearby magnetic fields (e.g., the
     * magnetic fields generated by nearby motors).
     * @return The current tilt-compensated compass heading, in degrees (0-360).
     */
     """

    def getCompassHeading(self):
        return self.compass_heading
    

    """
    /**
     * Sets the user-specified yaw offset to the current
     * yaw value reported by the nav6 IMU.
     * 
     * This user-specified yaw offset is automatically
     * subtracted from subsequent yaw values reported by
     * the getYaw() method.
     */
     """
    def zeroYaw(self):
        self.user_yaw_offset = self.getAverageFromYawHistory()
    

    """
    /**
     * Indicates whether the nav6 IMU is currently connected
     * to the host computer.  A connection is considered established
     * whenever a value update packet has been received from the
     * nav6 IMU within the last second.
     * @return Returns true if a valid update has been received within the last second.
     */
     """

    def isConnected(self):
        time_since_last_update = Timer.getFPGATimestamp() - self.last_update_time
        return (time_since_last_update <= 1.0)
    

    """
    /**
     * Returns the count in bytes of data received from the
     * nav6 IMU.  This could can be useful for diagnosing 
     * connectivity issues.
     * 
     * If the byte count is increasing, but the update count
     * (see getUpdateCount()) is not, this indicates a software
     * misconfiguration.
     * @return The number of bytes received from the nav6 IMU.
     */
     """

    def getByteCount(self):
        return self.byte_count
    

    """
    /**
     * Returns the count of valid update packets which have
     * been received from the nav6 IMU.  This count should increase
     * at the same rate indicated by the configured update rate.
     * @return The number of valid updates received from the nav6 IMU.
     */
     """

    def getUpdateCount(self):
        return self.update_count
    

    """
    /**
     * Returns true if the nav6 IMU is currently performing automatic
     * calibration.  Automatic calibration occurs when the nav6 IMU
     * is initially powered on, during which time the nav6 IMU should
     * be held still.
     * 
     * During this automatically calibration, the yaw, pitch and roll
     * values returned may not be accurate.
     * 
     * Once complete, the nav6 IMU will automatically remove an internal
     * yaw offset value from all reported values.
     * @return Returns true if the nav6 IMU is currently calibrating.
     */
     """

    def isCalibrating(self):
        calibration_state = self.flags & IMUProtocol.NAV6_FLAG_MASK_CALIBRATION_STATE
        return (calibration_state != IMUProtocol.NAV6_CALIBRATION_STATE_COMPLETE)
    

    """
    /**
     * Returns the current yaw value reported by the nav6 IMU.  This
     * yaw value is useful for implementing features including "auto rotate 
     * to a known angle".
     * @return The current yaw angle in degrees (-180 to 180).
     */
     """

    def pidGet(self):
        return self.getYaw()

    def updateTable(self):
        if (self.m_table != null) 
            self.m_table.putNumber("Value", getYaw())
        

    def startLiveWindowMode(self):
        pass
    

    def stopLiveWindowMode(self):
        pass
    

    def initTable(self, itable):
        self.m_table = itable
        self.updateTable()
    

    def getTable(self):
        return self.m_table
    

    def getSmartDashboardType(self):
        return "Gyro"
    

    #// Invoked when a new packet is received returns the packet length if the packet 
    #// is valid, based upon IMU Protocol definitions otherwise, returns 0
    
    def decodePacketHandler(self, received_data, offset, bytes_remaining):

        packet_length = IMUProtocol.decodeYPRUpdate(received_data, offset, bytes_remaining, self.ypr_update_data)
        if (packet_length > 0):
            self.setYawPitchRoll(self.ypr_update_data.yaw, self.ypr_update_data.pitch, self.ypr_update_data.roll, self.ypr_update_data.compass_heading)
        return packet_length
    
    #// IMU Class thread run method
    
    def run(self):

        stop = False
        stream_response_received = False
        last_stream_command_sent_timestamp = 0.0
        try:
            #self.serial_port.setReadBufferSize(512)
            self.serial_port.timeout = 1.0
            #self.serial_port.enableTermination('\n')
            self.serial_port.flush()
            #self.serial_port.reset()
        except Exception:
            printStackTrace()
                
        response = IMUProtocol.StreamResponse()

        stream_command = []
        
        cmd_packet_length = IMUProtocol.encodeStreamCommand( stream_command, update_type, update_rate_hz ) 
        try:
            #self.serial_port.reset()
            self.serial_port.write(stream_command)
            self.serial_port.flush()
            self.last_stream_command_sent_timestamp = Timer.getFPGATimestamp()
        except Exception:
                ex.printStackTrace()
        
        while (not stop):
            try:

                #// Wait, with delays to conserve CPU resources, until
                #// bytes have arrived.
                
                while ((not stop) and ( self.serial_port.getBytesReceived() < 1 ) ):
                    Timer.delay(0.1)

                packets_received = 0
                received_data = []
                received_data = self.serial_port.read(256)
                bytes_read = len(received_data)
                if (bytes_read > 0):
                    byte_count += bytes_read
                    i = 0
                    #// Scan the buffer looking for valid packets
                    while (i < bytes_read):
                                                
                        #// Attempt to decode a packet
                        
                        bytes_remaining = bytes_read - i
                        packet_length = self.decodePacketHandler(received_data,i,bytes_remaining)
                        if (packet_length > 0):
                            packets_received++
                            update_count++
                            i += packet_length
                        else:
                            packet_length = IMUProtocol.decodeStreamResponse(received_data, i, bytes_remaining, response)
                            if (packet_length > 0):
                                packets_received++
                                setStreamResponse(response)
                                stream_response_received = True
                                i += packet_length
                            else:
                                #// current index is not the start of a valid packet increment
                                i++
                
                    if ( ( packets_received == 0 ) and ( bytes_read == 256 ) ):
                        #// Workaround for issue found in Java SerialPort implementation:
                        #// No packets received and 256 bytes received this
                        #// condition occurs in the Java SerialPort.  In this case,
                        #// reset the serial port.
                        self.serial_port.reset()
                    
                    #// If a stream configuration response has not been received within three seconds
                    #// of operation, (re)send a stream configuration request
                    
                    if ( !stream_response_received and ((Timer.getFPGATimestamp() - last_stream_command_sent_timestamp ) > 3.0 ) ):
                        cmd_packet_length = IMUProtocol.encodeStreamCommand( stream_command, update_type, update_rate_hz )
                        try:
                            last_stream_command_sent_timestamp = Timer.getFPGATimestamp()
                            self.serial_port.write(stream_command)
                            self.serial_port.flush()
                        except Exception:
                                ex2.printStackTrace()
                    else:                      
                        #// If no bytes remain in the buffer, and not awaiting a response, sleep a bit
                        if ( stream_response_received == 0 ) ):
                            Timer.delay(1.0/update_rate_hz)
            except Exception:
                #// This exception typically indicates a Timeout
                stream_response_received = False
                ex.printStackTrace()


