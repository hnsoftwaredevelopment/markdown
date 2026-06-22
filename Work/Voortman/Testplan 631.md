- [Infeed](#infeed)
  - [Check material orientation](#check-material-orientation)
  - [Put on datum line](#put-on-datum-line)
    - [General tests](#general-tests)
    - [Test the typical flow](#test-the-typical-flow)
    - [Test alternative flows](#test-alternative-flows)
  - [Move into machine](#move-into-machine)
- [Drilling](#drilling)
  - [Basic test (typical):](#basic-test-typical)
  - [Extended test:](#extended-test)
- [Process](#process)


# Infeed
## Check material orientation
* Check that system asks to rotate material when it is in incorrect start view in the buffer (Alternative 1A)

## Put on datum line
### General tests
* Check how far material from datum line is still detected. 
This should be somewhere between 5-10 mm so it allows for bended beams, but is still close enough for other accuracy. 
Test with minimum and maximum material height for this machine (50mm-600mm?).

### Test the typical flow
* Create a nesting and select it for production
* Put corresponding material on the in feed
* Start
* Search material (use case step 2)
  * Check that material can be detected accurately by measuring the position were the drag dog goes up. (R4)

    Test with small flanges, wide flange and closed material. 
  
    Distance between where the drag dog goes up and the material should not differ more than 1 cm. 
    
    Distance between drag dog and material should always be more than 1 cm.
  * Check that drag dogs go all the way around, when they are not in or directly next to the rollers. The setting "Retrieve pusher" can be used to testing this. (R8).
* Put material on datum line (use case step 3)
  * Check that material pushed against datum line at less than full speed (R1)
  * Check that material is least touching 2 datum line rollers after is pushed against the datum line. (R2)
  Check that drag dogs move at slower speed when they are between the rollers and in up position in automatic mode (R3)
  * Check that drag dogs move at slower speed when they are between the rollers and in up position and operated manually (R3)
  * Check that material is pushed against the datum line with drag dogs behind material
  * Check that with small material with opening at bottom (e.g. UNP100) the drag dogs grabs material directly behind second flange.
  * Check that with wide material, with opening at the bottom (e.g. UNP200), drag dogs first pull behind the first flange, then put it on the datum when pushing second flange. (R7)
  * Check that with wide material, with no opening at the bottom (e.g. UNP 200 with legs up) the drag dogs grabs material directly behind second flange.
* Position of item is update in buffer
  * Check that position of item in buffer is update so it is now showing on the datum line
* Stop when machine tries to roll in towards machine

### Test alternative flows
**Alternative 1A**
  * Check if put on datum line is skipped when material on datum line sensor is activated. (When rest material is reused for a next batch it is not neceseaary to move the material to the datumloine. It is already there.)

**Alternative 1B**
  * Check that message is shown if material is too heavy for cross transport. For testing, the "Transport weight limit" could be temporarily changed, or a user profile could be created.
  * Check that automatic production is not started

**Alternative 2A**
  * Check material is not searched, but taken from theoretical position when it is in the in feed buffer with accurate position known. (R6)
  * Check material is searched, when it is in the in feed buffer but accurate position is not known.

**Alternative 2C**
  * Check that message is shown when material is not detected before it cross transport reaches the maximum axis position (with no configured maximum search position).
  * Check that message is shown when material is not detected before it cross transport reaches the configured maximum search position (which is smaller than maximum axis position).
  * Check that system stop after message is shown.
  * Check that system also stops if material can be detected, but out of reach of drag dogs (e.g. profile with closed bottom at end of cross transport).

**Alternative 2D**
  * Check that message is shown when photo cell is disabled. For testing, the user setting "Photocell present" can be used.
  * Check that automatic production is not started

**Alternative 4A**
  * Check that when pushing material on datum line and material on datum line sensor doesn't detect material, a message is shown.
  * Check that system stop after message is shown.

**Alternative 5A**
  * Check that machine shows a message when actual profile doesn't match theoretical. (R5)
  
    Test with both actual material being smaller and wider.
    E.g. test with theoretical profile UNP180  and actual profile UNP200 and test with theoretical profile UNP220  and actual profile UNP200

## Move into machine

  * Check that system skips moving material into machine, when it is already in at of front side measuring photo cells in the machine. (Alternative A1)
  * Check that machine show message when material is too heavy to be processed when material to be processed has a theorical weight of 16.000kg. It is probably necessary to create a user profile. (Alternative 1B)

# Drilling

## Basic test (typical):

  * Drill hole with each of the drill units
  * Drill center mark with each of the drill units

## Extended test:

Some of the tests require theoretical to be deliberately different(smaller or larger) than actual profile.

It might be necessary to manipulate measuring as well. E.g. by putting piece of flat material on the web, so web is measure higher at this position.

  * Drill hole with HSS. Check that suggested RPM and Feed are correct for this tool. Also check that actual feed and RPM match theoretical values. (R1)
  * Drill hole with HM. Check that suggested RPM and Feed are correct for this tool. Also check that actual feed and RPM match theoretical values. (R2)
  * Drill hole in different material grade. Check that actual feed and RPM match the specified feed and RPM for this other grade. (R3) In reality, standard material grade could be used to test this.
  * Drill hole with custom feed and RPM. Check that actual feed and RPM match the specified feed and RPM. (R4)
  * Check that it is possible to drill a blind hole. Check that the depth of the hole is correct, and the extra depth specified on the tool is not used. (R5)
  * Check that it is possible to drill a dual layer hole from the top in a tube. (R6)
  * Check that it is possible to drill and tap a threaded hole for a standard thread hole size (e.g 20 mm) (R7)
  * Check that it is possible to drill and tap a threaded hole for a custom thread hole size (e.g Test 21 mm and use 20 mm tools and parameters) (R8)
  * Check that it is possible to drill holes according to reference position. Test all 3 units, all 4 reference points (top, bottom, symmetry and absolute). (R9)
  * Check that it is possible to drill holes ignoring the reference position specified in the product. This should be possible by setting "Use measured profile width" to "No" and setting "Profile measurement method" to "None". (R9)
  * Check that it is possible to correct flange holes (with reference point symmetry) based on measure height of the web (use "Flange symmetry reference point" setting on machine). (R9) (This setting should be available, is probably missing!!!)
  * Check that it is possible to correct holes (with reference point symmetry) both in flanges differently using "Profile measurement method" "Multiple measure during profile check" (R9)
  * Check that it is possible to correct holes differently based on their x position in the beam using "Profile measurement method" "Single measure method using measure interval" (R9)

# Process