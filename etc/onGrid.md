# Topic

We chose *Candy* as our topic, since all of our subjects recognized popular candy brands and their attributes. The goal of our study was to figure out how our subjects perceived several popular candy brands.

# Procedure

1. Select three indivduals to be the subjects.
2. Interview one of the three subjects.
3. Ask the subject for ten examples of the topic.
4. Ask the subject for some attribute along which one of a group of three examples is different from the other two.
5. Ask the subject for two "ends" of the attribute to create a scale of 1 to 5, with 1 being the "bad"/"no" end and 5 being the "good"/"yes" end.
6. Ask the subject to rate all of the examples by the attribute.
7. Repeat steps 4-6 nine more times (to get ten attributes).
8. Repeat steps 2-7 for the remaining two subjects using the same ten examples from the first interview (to get ten separate attributes per subject for the same ten examples).
9. Turn each subject's responses into a csv file that can be read by a repgrid interpreter.
10. Run the repgrid interpreter on each csv file.
11. Analyze the results from the repgrid interpreter.

# Results

## Subject 1

The first subject chose *Skittles*, *KitKats*, *MAndMs*, *ReesesPeanutButterCups*, *DumDums*, *HersheysMilkChocolate*, *Twizzlers*, *HiChew*, *3Musketeers*, and *Gushers* as the examples and *IndividuallyPackaged*/*MultiPackaged*, *Solid*/*Gooey*, *PlainFlavor*/*VariedFlavors*, *Mild*/*Sweet*, *Disliked*/*Popular*, *Soft*/*Hard*, *PlainTexture*/*VariedTextures*, *Ordinary*/*Distinct*, *Unappealing*/*Appealing*, and *Cheap*/*Expensive* as the attributes. After running the repgrid interpreter, what made the most sense is that they seemed to rate examples by the attributes *PlainTexture*/*VariedTextures* and *Unappealing*/*Appealing*, as well as the attributes *Cheap*/*Expensive* and *IndividuallyPackaged*/*MultiPackaged*, similarly. This means that we could probably drop one of the attributes from each group of the those attributes. What's interesting is that they seemed to rank *HersheysMilkChocolate* and *KitKats* pretty differently than the rest of the examples.

## Subject 2

The second subject used the same ten examples from the first subject, but then chose *Chunky*/*Smooth*, *Mild*/*Intense*, *SmallBatch*/*LargeBatch*, *LowCocoaContent*/*HighCocoaContent*, *Bitter*/*Sweet*, *MeltsEasily*/*RemainsHard*, *LowQuality*/*HighQuality*, *Budget*/*Premium*, *Underrated*/*Popular*, and *Transparent*/*Opaque* as the attributes. After running the repgrid interpreter, what made the most sense is that they seemed to rate examples by the attributes *LowQuality*/*HighQuality* and *LowCocoaContent*/*HighCocoaContent*, as well as the attributes *Bitter*/*Sweet* and *Underrated*/*Popular*, similarly. This means that we could probably drop one of the attributes from each group of the those attributes. What's interesting is that they seemed to rank *HersheysMilkChocolate* and *HiChew* pretty differently than the rest of the examples.

## Subject 3

The third subject also used the same ten examples from the first subject, but then chose *Drab*/*Colorful*, *Fruity*/*Chocolatey*, *Crisp*/*Chewy*, *Soft*/*Crunchy*, *NotCircular*/*Circular*, *SinglePiece*/*Sectioned*, *Solid*/*Gooey*, *NotRed*/*Red*, *SingleFlavor*/*SeondaryFlavor*, and *Single*/*Multiple* as the attributes. After running the repgrid interpreter, what made the most sense is that they seemed to rate examples by the attributes *Solid*/*Gooey* and *Fruity*/*Chocolatey*, as well as the attributes *SinglePiece*/*Sectioned* and *SingleFlavor*/*SeondaryFlavor*, similarly. This means that we could probably drop one of the attributes from each group of the those attributes. What's interesting is that they seemed to rank *HersheysMilkChocolate* and *DumDums* pretty differently than the rest of the examples.

# Conclusion

All in all, we noticed that there weren't any attributes or ranking that were exactly the same between all of the subjects, but some examples and attributes were similarly grouped between subjects. For instance, the *Solid*/*Gooey* and *MeltsEasily*/*RemainsHard* attributes were pretty similar between subjects, as well as the rankings for *HersheysMilkChocolate*.