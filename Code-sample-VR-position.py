import openvr


def initialize_vr():
    try:
        # Initialize the VR system
        openvr.init(openvr.VRApplication_Scene)
        print("VR system initialized successfully!")

        vr_system = openvr.VRSystem()
        return vr_system
    except Exception as e:
        print(f"Error initializing VR system: {e}")
        return None


def get_headset_position(vr_system):
    # Get the pose (position and orientation) of the VR headset
    try:
        poses = vr_system.getDeviceToAbsoluteTrackingPose(
            openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount
        )
        headset_pose = poses[openvr.k_unTrackedDeviceIndex_Hmd]

        if headset_pose.bDeviceIsConnected and headset_pose.bPoseIsValid:
            pose_matrix = headset_pose.mDeviceToAbsoluteTracking
            position = (pose_matrix[0][3], pose_matrix[1][3], pose_matrix[2][3])
            return position
        else:
            return None
    except Exception as e:
        print(f"Error getting headset position: {e}")
        return None


def main():
    vr_system = initialize_vr()
    if vr_system:
        while True:
            position = get_headset_position(vr_system)
            if position:
                print(f"Headset position: x={position[0]:.2f}, y={position[1]:.2f}, z={position[2]:.2f}")
            else:
                print("Unable to get headset position.")
    else:
        print("Failed to initialize VR system.")


if __name__ == "__main__":
    main()
