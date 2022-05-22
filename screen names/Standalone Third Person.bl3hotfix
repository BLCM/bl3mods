###
### Name: StandAlone Third Person
### Author: screen names
### Version: 1.0
### Categories: qol, Resource, gameplay, bugfix
###
### License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
### License URL: https://creativecommons.org/licenses/by-sa/4.0/
### 

###
### Usage: Set the default camera to third person, Set the XYZ cordinates (change these to your liking!), Patch out some camera modes (stops events like sliding from switching to first person).
###

###
### Special thanks to apocalyptech for helping me throughout the development of this mod, I couldn't have done this without him.
###

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Edit the XYZ at the end of the line below to change the camera position.
SparkPatchEntry,(1,1,0,),/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson:CameraBehavior_OffsetCameraRelative_0,LocationOffset,0,,(x=-200,y=75,z=0)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Swap Camera Mode Names, effectively making the default camera 3rd person.
SparkPatchEntry,(1,1,0,),/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson,ModeName,0,,Default
SparkPatchEntry,(1,1,0,),/Game/GameData/Camera/CameraMode_Default.CameraMode_Default,ModeName,0,,ThirdPerson

# Patch out Certain Camera Modes, effectively stopping events from triggering the switch to that specific camera mode.
SparkPatchEntry,(1,1,0,),/Game/GameData/Camera/CameraModeSet_Default.CameraModeSet_Default,Modes,0,,(CameraMode_Default'"/Game/GameData/Camera/CameraMode_Default"',CameraMode_ThirdPerson'"/Game/GameData/Camera/CameraMode_ThirdPerson"',CameraMode_Fixed'"/Game/GameData/Camera/CameraMode_Fixed"',CameraMode_Orbit'"/Game/GameData/Camera/CameraMode_Orbit"',CameraMode_ThirdPersonViewModel'"/Game/GameData/Camera/CameraMode_ThirdPersonViewModel"',CameraMode_DownState'"/Game/GameData/Camera/CameraMode_DownState"',CameraMode_ThirdPersonNoInput'"/Game/GameData/Camera/CameraMode_ThirdPersonNoInput"',CameraMode_VehicleTransitionIn'"/Game/GameData/Camera/Vehicle/CameraMode_VehicleTransitionIn"',CameraMode_VehicleTransitionOut'"/Game/GameData/Camera/Vehicle/CameraMode_VehicleTransitionOut"',CameraMode_StatusMenu'"/Game/GameData/Camera/CameraMode_StatusMenu"',CameraMode_AIO'"/Game/GameData/Camera/CameraMode_AIO"',CameraMode_AIONoTranslucency'"/Game/GameData/Camera/CameraMode_AIONoTranslucency"',CameraMode_PhotoMode_Offset'"/Game/GameData/Camera/CameraMode_PhotoMode_Offset"',CameraMode_PhotoMode'"/Game/GameData/Camera/CameraMode_PhotoMode"',CameraMode_Mission1_CameraStart'"/Game/Missions/Plot/EP01_ChildrenOfTheVault/CameraMode_Mission1_CameraStart"',CameraMode_Mission1_EchoDevice'"/Game/Missions/Plot/EP01_ChildrenOfTheVault/CameraMode_Mission1_EchoDevice"',CameraMode_Mission1_EULA'"/Game/Missions/Plot/EP01_ChildrenOfTheVault/CameraMode_Mission1_EULA"',CamMode_Shared_Teleport'"/Game/PlayerCharacters/_Shared/_Design/PlayerTeleport/CamMode_Shared_Teleport"',CameraMode_RaidSpectator'"/Game/GameData/Camera/CameraMode_RaidSpectator"',CameraMode_Mission1_CameraStart'"/Game/Missions/Plot/EP01_ChildrenOfTheVault/CameraMode_Mission1_CameraStart"')

# Add zoom behavior to CameraMode_ThirdPerson
SparkPatchEntry,(1,1,0,),/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson,Behaviors,0,,(CameraBehavior_Look'/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson:CameraBehavior_Look_0',CameraBehavior_LimitPitch'/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson:CameraBehavior_LimitPitch_0',CameraBehavior_DefaultFOV'/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson:CameraBehavior_DefaultFOV_0',CameraBehavior_AnchorToEyeLocation'/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson:CameraBehavior_AnchorToEyeLocation_1',CameraBehavior_OffsetCameraRelative'/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson:CameraBehavior_OffsetCameraRelative_0',CameraBehavior_CollisionOffsetTrace'/Game/GameData/Camera/CameraMode_ThirdPerson.CameraMode_ThirdPerson:CameraBehavior_CollisionOffsetTrace_0',CameraBehavior_WeaponZoomFOV'/Game/GameData/Camera/CameraMode_Default.CameraMode_Default:CameraBehavior_WeaponZoomFOV_0')
