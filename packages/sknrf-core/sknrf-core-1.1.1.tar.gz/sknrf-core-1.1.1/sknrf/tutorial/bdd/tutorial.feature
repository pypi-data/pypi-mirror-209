# Run "behave" from this directory to execute the test
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      when we implement a test
      then behave will test it for us!

  Scenario Outline: Blenders
   Given I put <thing> in a blender,
    when I switch the blender on
    then it should transform into <other thing>

 Examples: Amphibians
   | thing         | other thing |
   | Red Tree Frog | mush        |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |