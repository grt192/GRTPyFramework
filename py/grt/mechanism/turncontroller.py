from time import sleep
def turn(amount, measured):
    p_error = amount
    integ = 0
    dt = 0.01
    Kp = Ki = Kd = 1 #tentative, need to tune variables
    while(p_error > 0.01): #0.01 is arbitrary, we can get as close as we need to
        error = amount - measured
        integ += error * dt
        deriv = (error - p_error)/dt
        out = Kp * error + Ki * integ + Kd * deriv #output to motor 
        p_error = error
        sleep(dt)
