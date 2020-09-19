import maya.cmds as cmds

def run ():

    # Sticky Mod
    try:
        cmds.frameLayout ('jsap_stickyMod_fl', e = 1, cl = False)
        cmds.floatField ('jsap_sm_falloff_ff', e = 1, v = 1.0)
        cmds.intField ('jsap_sm_smooth_if', e = 1, v = 3)
        cmds.optionMenu ('jsap_sm_vis_om', e = 1, sl = 1)
        cmds.floatField ('jsap_sm_scale_ff', e = 1, v = 1.0)
        cmds.checkBox ('jsap_sm_sphere_cb', e = 1, v = True)
        cmds.checkBox ('jsap_sm_lra_cb', e = 1, v = False)
        cmds.checkBox ('jsap_sm_forceDisplay_cb', e = 1, v = True)
    except:
        pass

    # Sculpt Pose
    try:
        cmds.frameLayout ('jsap_sculptPose_fl', e = 1, cl = False)
        cmds.checkBox ('jsap_scuVis_cb', e = 1, v = True)
        cmds.checkBox ('jsap_scuReshade_cb', e = 1, v = True)
        cmds.checkBox ('jsap_scuData_cb', e = 1, v = True)
        cmds.intField ('jsap_scuLevel_if', e = 1, v = 1)
        cmds.optionMenu ('jsap_sfz_om', e = 1, sl = 1)
    except:
        pass

    # Wrap ++
    try:
        cmds.frameLayout ('jsap_wrap_fl', e = 1, cl = False)
        cmds.intField ('jsap_wrap_autoSmooth_if', e = 1, v = 3)
    except:
        pass

