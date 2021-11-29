# Apex-mprt-importer-for-Blender
Import Apex legends mprt files exported from Legion.  

# [*REQUIRES CAST IMPORTER*](https://github.com/dtzxporter/cast)

# Usage:
1. Use a VPK extracter to extract the map BSP from vpk. (Eg. [Titanfall_VPKTool](https://github.com/Wanty5883/Titanfall2/blob/master/tools/Titanfall_VPKTool3.4_Portable.zip))
2. Open corresponding .rpak with [Legion](https://wiki.modme.co/wiki/apps/Legion.html) using cast, then load BSP. It will auto export the BSP models and generate a mprt file.
3. Use Legion to extract all model files.
4. Install the Apex mprt importer, the UI is in the viewport sidebar.
5. Select the map mprt file and the model directory. Recommended: Use game coordinates to set the map region and an import radius.
6. Optional: Choose name filter objects to skip import, eg. godray, grass, bush
7. Open console and import map. Import time will increase drastically with map size importing full large maps not recommended.
8. When the map is imported it will be very large, increase the view clip distance and zoom out to see map.
9. Enjoy.


![e02234fb1e88a9750a59ed33656547f5](https://user-images.githubusercontent.com/38115052/143941621-03ecee92-d015-4133-9c09-cf6014160c9c.png)
