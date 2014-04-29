GRTPyFramework
==============

GRTFramework for Python, for event-based robotics programming.

Introduction:
=============

Beyond basic framework and abstractions, GRTPyFramework provides a method by which more sophisticated logic and
abstractions can be developed, provided a particular code structure is followed in line with design methodology.

Details:
========

User code is split into two parts: mechanisms, and controllers.

Mechanisms:
-----------

Mechanisms are collections of sensors and actuators that represent a specific robot assembly, providing an API by which
that assembly can be controlled globally, as opposed to in terms of its individual parts. Mechanisms should not operate
on their own, simply translating abstract commands into specific hardware directives. Mechanisms may be nested, and also
may provide closed loop operation (limit switch logic, etc.)

Controllers:
------------

Controllers are governing objects that provide instructions for the various mechanisms on a robot. A controller contains
the logic necessary to tell a mechanism what to do. A controller may operate over one or more mechanisms,
defining the logic by which each assembly is used. Controllers may be fully autonomous or draw on sensor or user
feedback to command Mechanisms in the appropriate way. As a matter of abstraction, Controllers should never have direct
access to Sensors or Actuators.

Flow Diagram:

    Controller
       |
       '--- Mechanism
                   |
                   |--- Actuator(s)
                   '--- Sensor(s)

Sensor Feedback
---------------

#### Sensors:

Sensors help the robot to sense its state and environment. For example, a potentiometer may be used to determine the
rotation undergone by an axle (robot state), while a distance sensor may be used to sense the robot's location in
relation to a field (environment).

Sensors have listeners;