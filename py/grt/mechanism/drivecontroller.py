"""
Module for various drivetrain control mechanisms.
Listens to Attack3Joysticks, not wpilib.Joysticks.
"""
from collections import OrderedDict

class ArcadeDriveController:
    """
    Class for controlling DT in arcade drive mode, with one or two joysticks.
    """

    def __init__(self, dt, l_joystick, record_macro=None, playback_macro=None, r_joystick=None):
        """
        Initialize arcade drive controller with a DT and up to two joysticks.
        """
        self.dt = dt
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        self.record_macro = record_macro
        self.playback_macro = playback_macro

        #Should be the one-tote auto instructions
        #self.instructions = OrderedDict([("1, <class 'wpilib.cantalon.CANTalon'>", [-0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, 0.04594330400782014, 0.0, 0.0, 0.0, -0.07038123167155426, -0.3704789833822092, -0.5581622678396871, -0.6373411534701857, -0.5034213098729228, -0.46432062561094817, -0.5268817204301075, -0.5112414467253177, -0.41642228739002934, -0.3460410557184751, -0.3304007820136852, -0.3069403714565005, -0.3069403714565005, -0.2913000977517107, -0.2678396871945259, -0.2678396871945259, -0.2678396871945259, -0.3304007820136852, -0.3460410557184751, -0.36950146627565983, -0.2668621700879765, -0.007820136852394917, 0.022482893450635387, 0.022482893450635387, 0.022482893450635387]), ("7, <class 'wpilib.cantalon.CANTalon'>", [-0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, 0.04594330400782014, 0.0, 0.0, 0.0, 0.039100684261974585, 0.4946236559139785, 0.5581622678396871, 0.5747800586510264, 0.44086021505376344, 0.47996089931573804, 0.41642228739002934, 0.40078201368523947, 0.41642228739002934, 0.3616813294232649, 0.37732160312805474, 0.35386119257087, 0.35386119257087, 0.33822091886608013, 0.3616813294232649, 0.3616813294232649, 0.3616813294232649, 0.2825024437927664, 0.2825024437927664, 0.2590420332355816, 0.20430107526881722, 0.10166177908113393, 0.022482893450635387, 0.022482893450635387, 0.022482893450635387]), ("100, <class 'grt.macro.assistance_macros.ElevatorMacro'>", [0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0])])

        #Junk bin stealer instructions
        #self.instructions = OrderedDict([("1, <class 'wpilib.cantalon.CANTalon'>", [0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.030303030303030304, -0.10948191593352884, -0.21212121212121213, -0.22776148582600195, -0.0469208211143695, -0.10166177908113393, -0.12512218963831867, -0.093841642228739, -0.14076246334310852, -0.06256109481915934, -0.03128054740957967, -0.093841642228739, -0.093841642228739, -0.20430107526881722, -0.20430107526881722, -0.22776148582600195, -0.12512218963831867, -0.093841642228739, -0.093841642228739, -0.093841642228739, -0.093841642228739, -0.015640273704789834, 0.0, 0.0, 0.006842619745845552, 0.053763440860215055, 0.13196480938416422, 0.18670576735092864, 0.14760508308895406, 0.14760508308895406, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.14760508308895406, 0.14760508308895406, 0.14760508308895406, 0.14760508308895406, 0.14760508308895406, 0.14760508308895406, 0.08504398826979472, 0.006842619745845552, 0.1710654936461388, 0.18670576735092864, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.2101661779081134, 0.14760508308895406, 0.14760508308895406, 0.14760508308895406, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552]), ("7, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01466275659824047, 0.15640273704789834, 0.2590420332355816, 0.27468230694037143, 0.093841642228739, -0.039100684261974585, -0.06256109481915934, -0.093841642228739, 0.07820136852394917, 0.0, -0.03128054740957967, -0.093841642228739, -0.093841642228739, 0.015640273704789834, 0.015640273704789834, 0.039100684261974585, -0.06256109481915934, -0.093841642228739, -0.093841642228739, -0.093841642228739, -0.093841642228739, -0.015640273704789834, 0.0, 0.0, -0.006842619745845552, -0.03812316715542522, -0.11632453567937438, -0.1710654936461388, -0.13196480938416422, -0.13196480938416422, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.13196480938416422, -0.13196480938416422, -0.13196480938416422, -0.13196480938416422, -0.13196480938416422, -0.13196480938416422, -0.08504398826979472, -0.006842619745845552, -0.15542521994134897, -0.1710654936461388, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.19452590420332355, -0.13196480938416422, -0.13196480938416422, -0.13196480938416422, 0.02346041055718475, 0.006842619745845552, 0.006842619745845552]), ("100, <class 'grt.macro.assistance_macros.ElevatorMacro'>", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])

        #Bin stealer auto instructions
        #self.instructions = OrderedDict([("1, <class 'wpilib.cantalon.CANTalon'>", [-0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, 0.022482893450635387, 0.022482893450635387, 0.030303030303030304, 0.030303030303030304, 0.030303030303030304, 0.030303030303030304, 0.030303030303030304, 0.030303030303030304, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.0469208211143695, -0.08602150537634409, -0.18866080156402737, -0.12512218963831867, -0.08602150537634409, -0.03128054740957967, -0.08602150537634409, -0.20430107526881722, -0.10948191593352884, -0.08602150537634409, 0.0, 0.006842619745845552, -0.08602150537634409, -0.20430107526881722, -0.0469208211143695, -0.05474095796676442, -0.05474095796676442, -0.05474095796676442, -0.07038123167155426, -0.07038123167155426, -0.07038123167155426, -0.07038123167155426, -0.12512218963831867, -0.08602150537634409, -0.14076246334310852, -0.093841642228739, -0.02346041055718475, 0.06158357771260997, 0.13978494623655913, 0.20234604105571846, 0.08504398826979472, 0.13978494623655913, 0.13978494623655913, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.14760508308895406, 0.022482893450635387, 0.10850439882697947, 0.10850439882697947, 0.14760508308895406, 0.1710654936461388, 0.18670576735092864, 0.1241446725317693, 0.10850439882697947, 0.10850439882697947, 0.18670576735092864, 0.18670576735092864, 0.18670576735092864, 0.18670576735092864, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.20234604105571846, 0.22580645161290322, 0.1710654936461388, 0.1710654936461388, 0.1710654936461388, 0.14760508308895406, 0.022482893450635387, 0.022482893450635387, 0.022482893450635387]), ("7, <class 'wpilib.cantalon.CANTalon'>", [-0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, 0.022482893450635387, 0.022482893450635387, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.07820136852394917, 0.093841642228739, 0.13294232649071358, 0.23558162267839688, 0.06256109481915934, 0.02346041055718475, -0.03128054740957967, 0.02346041055718475, 0.06256109481915934, 0.07820136852394917, 0.05474095796676442, 0.0, 0.006842619745845552, 0.10166177908113393, 0.21994134897360704, 0.06256109481915934, -0.05474095796676442, -0.05474095796676442, -0.05474095796676442, 0.07038123167155426, 0.07038123167155426, 0.07038123167155426, 0.07038123167155426, 0.015640273704789834, 0.05474095796676442, 0.0, -0.093841642228739, -0.006842619745845552, -0.06158357771260997, -0.13978494623655913, -0.20234604105571846, -0.19550342130987292, -0.13978494623655913, -0.13978494623655913, -0.20234604105571846, -0.20234604105571846, -0.20234604105571846, -0.20234604105571846, -0.20234604105571846, -0.25806451612903225, -0.022482893450635387, -0.09286412512218964, -0.09286412512218964, -0.13196480938416422, -0.15542521994134897, -0.13978494623655913, -0.0772238514173998, -0.06158357771260997, -0.06158357771260997, -0.13978494623655913, -0.13978494623655913, -0.13978494623655913, -0.13978494623655913, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.15542521994134897, -0.17888563049853373, -0.23460410557184752, -0.23460410557184752, -0.23460410557184752, -0.11632453567937438, 0.022482893450635387, 0.022482893450635387, 0.022482893450635387]), ("100, <class 'grt.macro.assistance_macros.ElevatorMacro'>", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ("5, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.6999022482893451, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])])

        #Should be instructions for stack macro. Not yet tested!
        #self.instructions = OrderedDict([("1, <class 'wpilib.cantalon.CANTalon'>", [-0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, -0.0469208211143695, 0.030303030303030304, 0.10850439882697947, 0.19452590420332355, 0.08504398826979472, 0.006842619745845552, 0.06940371456500488, 0.10850439882697947, 0.13196480938416422, 0.06940371456500488, 0.01466275659824047, 0.01466275659824047, 0.13196480938416422, 0.14760508308895406, 0.053763440860215055, 0.053763440860215055, 0.030303030303030304, 0.08504398826979472, 0.10850439882697947, 0.1241446725317693, 0.022482893450635387, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, -0.02346041055718475, -0.02346041055718475, -0.06256109481915934, -0.22776148582600195, -0.2434017595307918, -0.06256109481915934, 0.006842619745845552, 0.006842619745845552, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.01466275659824047, 0.10850439882697947, 0.2101661779081134, 0.06158357771260997, 0.06158357771260997, 0.17888563049853373, 0.20234604105571846, 0.13978494623655913, 0.006842619745845552, 0.006842619745845552, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917, -0.007820136852394917]), ("7, <class 'wpilib.cantalon.CANTalon'>", [-0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.03128054740957967, -0.03128054740957967, -0.03128054740957967, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.015640273704789834, -0.093841642228739, -0.25024437927663734, -0.2570869990224829, -0.08504398826979472, 0.006842619745845552, -0.053763440860215055, -0.09286412512218964, -0.11632453567937438, -0.053763440860215055, 0.0, 0.0, -0.11632453567937438, -0.13196480938416422, -0.03812316715542522, -0.03812316715542522, -0.01466275659824047, -0.11730205278592376, -0.13978494623655913, -0.1241446725317693, -0.022482893450635387, -0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.006842619745845552, 0.039100684261974585, 0.039100684261974585, 0.07820136852394917, 0.2434017595307918, 0.2590420332355816, 0.07820136852394917, 0.006842619745845552, 0.006842619745845552, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.01466275659824047, -0.19452590420332355, -0.06158357771260997, -0.06158357771260997, -0.17888563049853373, -0.20234604105571846, -0.13978494623655913, 0.006842619745845552, 0.006842619745845552, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475, 0.02346041055718475]), ("100, <class 'grt.macro.assistance_macros.ElevatorMacro'>", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22]), ("5, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])])

        #Better pickup macro instructions
        #self.instructions = OrderedDict([("1, <class 'wpilib.cantalon.CANTalon'>", [-0.04398826979472141, -0.04398826979472141, -0.011730205278592375, -0.10654936461388075, -0.11925708699902249, 0.04985337243401759, 0.09970674486803519, 0.0, -0.05571847507331378, -0.05571847507331378, 0.005865102639296188, -0.005865102639296188, -0.005865102639296188]), ("7, <class 'wpilib.cantalon.CANTalon'>", [-0.04398826979472141, -0.04398826979472141, -0.011730205278592375, 0.10654936461388075, 0.13196480938416422, -0.04985337243401759, -0.09970674486803519, 0.0, -0.05571847507331378, -0.05571847507331378, 0.005865102639296188, 0.01857282502443793, 0.01857282502443793]), ("100, <class 'grt.macro.assistance_macros.ElevatorMacro'>", [0, 0, 0, 0, 0, 0, 22, 22, 22, 22, 22, 22, 22]), ("5, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])])

        #Teleop can placement instructions
        self.disabled = False
        self.instructions = OrderedDict([("1, <class 'wpilib.cantalon.CANTalon'>", [-0.01857282502443793, -0.01857282502443793, -0.01857282502443793, 0.01857282502443793, 0.05571847507331378, 0.01857282502443793, -0.04398826979472141, -0.011730205278592375, 0.06842619745845552, 0.11241446725317693, 0.1935483870967742, 0.1935483870967742, 0.21212121212121213, 0.22482893450635386, 0.22482893450635386, 0.22482893450635386, 0.22482893450635386, 0.1436950146627566, -0.03714565004887586, 0.011730205278592375]), ("7, <class 'wpilib.cantalon.CANTalon'>", [-0.03128054740957967, -0.03128054740957967, -0.03128054740957967, 0.01857282502443793, -0.030303030303030304, 0.01857282502443793, -0.04398826979472141, 0.011730205278592375, -0.06842619745845552, -0.15640273704789834, -0.1935483870967742, -0.1935483870967742, -0.22482893450635386, -0.22482893450635386, -0.22482893450635386, -0.22482893450635386, -0.22482893450635386, -0.18084066471163246, -0.04985337243401759, 0.0]), ("100, <class 'grt.macro.assistance_macros.ElevatorMacro'>", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ("5, <class 'wpilib.cantalon.CANTalon'>", [0.0, 0.0, 0.0, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, -0.4995112414467253, 0.0, 0.0, 0.0])])

        self.engage()

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.l_joystick, self.r_joystick) and state_id in ('x_axis', 'y_axis'):
            power = -self.l_joystick.y_axis * .8
            turnval = (self.r_joystick.x_axis if self.r_joystick else self.l_joystick.x_axis) * .8
            # get turn value from r_joystick if it exists, else get it from l_joystick
            #print("Power: %f" % power)
            self.dt.drive_controller_set_dt_output(power + turnval, power - turnval)
        elif sensor == self.l_joystick and state_id == 'trigger':
            if datum:
                self.dt.upshift()
            else:
                self.dt.downshift()
        if state_id == "button11":
            if datum:
                print("Recording started")
                self.record_macro.start_record()
        if state_id == "button10":
            if datum:
                print("Recording stopped")
                self.record_macro.stop_record()
                #self.record_macro.instructions = self.instructions
        if state_id == "button9":
            if datum:
                self.playback_macro.start_playback(self.instructions)
        if state_id == "button8":
            if datum:
                self.playback_macro.stop_playback()
        if state_id == "button70":
            if datum:
                self.playback_macro.load("/home/lvuser/py/instructions.py")
                self.playback_macro.start_playback()

    def disable(self):
        self.disabled = True
    def enable(self):
        self.disabled = False

    def engage(self):
            self.l_joystick.add_listener(self._joylistener)
            if self.r_joystick:
                self.r_joystick.add_listener(self._joylistener)

    def disengage(self):
            self.l_joystick.remove_listener(self._joylistener)
            if self.r_joystick:
                self.r_joystick.remove_listener(self._joylistener)

class TankDriveController:
    """
    Class for controlling DT in tank drive mode with two joysticks.
    """

    def __init__(self, dt, l_joystick, r_joystick):
        """
        Initializes self with a DT and left and right joysticks.
        """
        self.dt = dt
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        l_joystick.add_listener(self._joylistener)
        r_joystick.add_listener(self._joylistener)

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.l_joystick, self.r_joystick) and state_id in ('x_axis', 'y_axis'):
            self.dt.set_dt_output(self.l_joystick.y_axis,
                                  self.r_joystick.y_axis)