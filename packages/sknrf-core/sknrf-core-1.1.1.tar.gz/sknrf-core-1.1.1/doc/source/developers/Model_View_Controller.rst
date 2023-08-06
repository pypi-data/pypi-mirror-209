Model, View, Controller (MVC) Programming
=========================================


Model, View, Controller (MVC)
-----------------------------
Model, View, Controller is a programming technique that separates the "logic" from the "user-interface":

..  figure:: ../_images/PNG/mvc_theory.png
    :width: 50 %
    :align: center

    Theoretical Model, View, Controller Design Pattern

Model
~~~~~

The Model encapsulates a logical building block (back-end) of the code and encapsulates the following information:

- Properties: The state of the buiding block (object).
- Methods: The operations that a building block can perform.
- Events: Signals that are emitted to communicate asynchronously with the outside world.

View
~~~~

The View is the user-interface (front-end) of the code that provides the user with an interactive application. It
performs the following tasks:

- Displays the contents of the model.
- Responds to the user-input.

Controller (Delegate)
~~~~~~~~~~~~~~~~~~~~~

The Controller orchestrates the communication between the Model and View and ensures that they remain synchronized. The
concept of the Controller satisfies applications that distinguish between a display (the View) and an instrumentation panel
(the Controller), however this is overcomplicated for computer applications where the instrumentation panel is built into
the user-interface (the View). In these situations the Controller is simply a delagate that is used to communicate
information between the Model and the View.


Multi-Threading/Multi-Processing Design Patterns
------------------------------------------------

The Observer and Publish/Subscribe design patterns are similar concepts that provide a more explicit definition of how
the Model and View update each other even when they are defined in separate threads or processes. Thus, in order to
communicate between the Model, View and Controller in a multi-threaded/multi-processing application, the Qt Framework
provides a Signal/Slot mechanism to send/receive messages and data.

Signals
~~~~~~~

Qt Signals are interrupts (or events) that encapsulate the information that is transmitted between the Model, View, or Controller.

Slots
~~~~~

Qt Slots are callback methods that receive signals and provide an asynchronous response to an event that has occurred somewhere else.


Multi-Threading
---------------

Multi-threading is difficult to achieve using interpreted programming languages because the interpreter locks while
executing each instruction. Although Python provides a multi-threading library, the Qt Framework multi-threading is
preferable because it is implemented in C++.

There are several design patterns of multi-threading tailored to different problems based on the severity of the following
requirements:

- Parallel instruction execution.
- Parallel data access.

Measurement Runtime MVC Multi-Threading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During a long automated measurement process, multi-threading must:

- Synchronize data between the model and view.
- Enable interactive display of the measurement data.
- Provide start/step/pause/stop runtime state.

..  figure:: ../_images/PNG/mvc_runtime.png
    :width: 50 %
    :align: center

    Measurement Runtime Model, View, Controller Design Pattern Simplification

A custom runtime measurement experience can be implemented by inheriting the following classes:

- :py:class:`RuntimeModel <sknrf.model.runtime.RuntimeModel>` (Model).
- :py:class:`RuntimeView <sknrf.view.desktop.runtime.runtime.RuntimeView>` (A Global Enum).

The multi-threaded runtime environment is controlled by the following classes:

- :py:class:`RuntimeThread <sknrf.model.runtime.RuntimeThread>` (Controller).
- :py:class:`RuntimeState <sknrf.device.base.RuntimeState>` (A Global Enum).

Hence, this implementaion is a simplification of the theoretical MVC design pattern and is suited towards measurement applications.


Comparison of Automated Measurement Techniques
----------------------------------------------
Three incremental solutions are available for measurement automation:

1. Sequencer.
2. Scripting.
3. Application.

The MVC programming design pattern enables code re-use and refinement to move between these three solutions by separating
the model (the logic) from the view (the user interface). Each solution has different limitations on customization as
summarized below:

.. raw:: html

   <table width="100%">
    <tr>
        <th width="20%"> Solution Type </th>
        <th width="20%"> View </th>
        <th width="20%"> Controller </th>
        <th width="20%"> Model </th>
    </tr>
    <tr>
        <td><a href="./Sequencer">Sequencer</a></td>
        <td><a href="../internal/api/sknrf.view.desktop.runtime.runtime.RuntimeView.html#sknrf.view.desktop.runtime.runtime.RuntimeView"> Default RuntimeView</a></td>
        <td><a href="../internal/api/sknrf.model.runtime.RuntimeThread.html#sknrf.model.runtime.RuntimeThread">RuntimeThread</a></td>
        <td><a href="../internal/api/sknrf.model.runtime.RuntimeModel.html#sknrf.model.runtime.RuntimeThread">RuntimeModel Sequencer Actions</a></td>
    </tr>
    <tr>
        <td><a href="./Scripting">Sequencer</a></td>
        <td>Jupyter Notebook</td>
        <td>None/td>
        <td><a href="../internal/api/sknrf.model.runtime.RuntimeModel.html#sknrf.model.runtime.RuntimeThread">Custom RuntimeModel</a></td>
    </tr>
    <tr>
        <td><a href="./Application">Application</a></td>
        <td><a href="../internal/api/sknrf.view.desktop.runtime.runtime.RuntimeView.html#sknrf.view.desktop.runtime.runtime.RuntimeView">Custom RuntimeView</a></td>
        <td><a href="../internal/api/sknrf.model.runtime.RuntimeThread.html#sknrf.model.runtime.RuntimeThread">RuntimeThread</a></td>
        <td><a href="../internal/api/sknrf.model.runtime.RuntimeModel.html#sknrf.model.runtime.RuntimeThread">Custom RuntimeModel</a></td>
    </tr>
   </table>

RuntimeModel Sequencer Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Sequencer searches through installed modules and will expose any public method of a class that inherits from
:py:class:`RuntimeModel <sknrf.model.runtime.RuntimeModel>` as a Sequencer Action.
