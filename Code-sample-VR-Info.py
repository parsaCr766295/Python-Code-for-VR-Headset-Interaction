import openvr

def initialize_vr():
    # تلاش برای راه‌اندازی OpenVR
    try:
        openvr.init(openvr.VRApplication_Scene)
        print("هدست واقعیت مجازی با موفقیت راه‌اندازی شد.")
    except Exception as e:
        print("خطا در راه‌اندازی VR:", e)
        return None
    return openvr

def get_vr_system_info():
    vr_system = openvr.VRSystem()
    if vr_system:
        # نمایش اطلاعات مختصر از هدست
        print("نام هدست:", vr_system.getStringTrackedDeviceProperty(0, openvr.Prop_TrackingSystemName_String))
        print("مدل دستگاه:", vr_system.getStringTrackedDeviceProperty(0, openvr.Prop_ModelNumber_String))
        print("سریال دستگاه:", vr_system.getStringTrackedDeviceProperty(0, openvr.Prop_SerialNumber_String))
    else:
        print("سیستم واقعیت مجازی پیدا نشد!")

def shutdown_vr():
    openvr.shutdown()
    print("سیستم واقعیت مجازی متوقف شد.")

# اجرای کد
if __name__ == "__main__":
    vr_context = initialize_vr()
    if vr_context:
        get_vr_system_info()
        shutdown_vr()
