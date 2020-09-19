'''

Written by Josh Sobel
joshsobel89@gmail.com
http://www.joshsobelrigs.com

Run with:

import js_animPolish.js_animPolish_ui as js_animPolish_ui
reload (js_animPolish_ui)
js_animPolish_ui.ui()

'''



import maya.cmds as cmds
import maya.mel as mel
import sys
import os
import js_animPolish.js_sculptPose as js_sculptPose
import js_animPolish.js_wrap as js_wrap
import js_animPolish.js_stickyMod as js_stickyMod
import js_animPolish as jsap
reload (js_sculptPose)
reload (js_wrap)
reload (js_stickyMod)
reload (jsap)



##########
### UI ###
##########



def ui (dock = 1):

	# Define
	win = 'js_animPolish'
	dockUI = 'js_animPolish_dock'
	width = 275
	height = 260
	bWidth = width - 37
	bHeight = 35
	bHeight2 = bHeight * .6
	bColor_green = [0.670,0.736,0.602]
	bColor_blue = [0.571,0.676,0.778]
	bColor_purple = [0.691,0.604,0.756]
	bColor_red = [0.765,0.525,0.549]
	bColor_brown = [0.804,0.732,0.646]
	if (cmds.window (win, exists = 1)):
		cmds.deleteUI (win)
	if (cmds.dockControl (dockUI, exists = 1)):
		cmds.deleteUI (dockUI)
	cmds.window (win, rtf = 0, t = 'Sticky Deformer', s = 0, w = width+20)

	"""

	# Header
	try:
		cmds.scrollLayout ('jsap_scroll', vsb = 1, w = width+20)
	except:
		cmds.scrollLayout ('jsap_scroll')
	cmds.columnLayout (adj = 1, rs = 3, w = width)
	cmds.separator (h = 7, style = 'none', w = width+20)
	cmds.text (l = "AnimPolish BASIC v1.00", font = 'boldLabelFont')
	cmds.text (l = "Deformation Tools For Animators\nand Simulation Artists")
	cmds.separator (h = 7, style = 'none')
	cmds.text (l = "Hover over any button/element for instructions in Maya's status bar.", ww = 1)
	cmds.separator (h = 11, style = 'none')
	cmds.iconTextButton (l = '        Unlock AnimPolish PREMIUM!', i = 'animateSnapshot.png', bgc = bColor_green, st = 'iconAndTextHorizontal', ann = "Unlock access to the full set of AnimPolish tools!", h = bHeight+10, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish')")
	cmds.separator (h = 11, style = 'none')
	cmds.iconTextButton (l = '                     Toggle DG/Parallel', i = 'bufferSwap.png', bgc = bColor_green, st = 'iconAndTextHorizontal', ann = "It's recommended to use these tools in the 'DG' animation evaluation mode. 'Parallel' mode may yield unstable results.", h = bHeight2, c = "import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.toggleAnimEval ()")
	cmds.iconTextButton (l = '                          Save Settings', i = 'fileSave.png', bgc = bColor_blue, st = 'iconAndTextHorizontal', ann = "Saves current AnimPolish UI settings so that they remain the same when you re-open it later.", h = bHeight2, c = "import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.saveSettings ()")
	cmds.iconTextButton (l = '                        Default Settings', i = 'undo_s.png', bgc = bColor_blue, st = 'iconAndTextHorizontal', ann = "Resets default UI settings.", h = bHeight2, c = "import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.defaultSettings ()")
	cmds.separator (h = 6, style = 'double')
	cmds.iconTextButton (l = '                        Documentation', i = 'help.png', bgc = bColor_brown, ann = 'Detailed instructions for each tool.', st = 'iconAndTextHorizontal', h = bHeight2, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish-documentation')")
	cmds.iconTextButton (l = '                     Check For Updates', i = 'refresh.png', bgc = bColor_brown, ann = 'Check for latest download.', st = 'iconAndTextHorizontal', h = bHeight2, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish-updates')")
	cmds.iconTextButton (l = '                              Contact', i = 'fileTextureEdit.png', bgc = bColor_brown, ann = 'Email Josh about bugs and such.', st = 'iconAndTextHorizontal', h = bHeight2, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/contact')")
	cmds.separator (h = 6, st = 'none')
	cmds.setParent ('..')
"""
	# Sticky Mod
	cmds.frameLayout ('jsap_stickyMod_fl', l = 'Sticky Mod', cll = 0, cl = 1, mh = 8, mw = 15, w = width, ann = "Ride-along manipulator with adjustable falloff and placement for quick mesh adjustments.\nThis tool uses Handles and Nurbs Curves, which are turned on automatically if 'Force Display' is on.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '            Create Sticky Mod *', i = 'locator.png', bgc = bColor_green, ann = "Creates a ride-along manipulator with adjustable falloff for quick mesh adjustments.\n* Select 1 vertex to run, or multiple vertices to ignore interactive falloff and auto-flood/smooth the map. When running on multiple, the rivet will be built on the last vert in the selection.\nThis tool uses Handles and Nurbs Curves, which are turned on automatically if 'Force Display' is on.", st = 'iconAndTextHorizontal', w = bWidth, h = bHeight, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.sm_create ()')
	cmds.rowColumnLayout (nc = 2, rs = [2,3], cs = [2,3])
	cmds.button (l = 'Add Geo', bgc = bColor_brown, ann = 'Add selected geo to selected sticky mod.', w = (width/2), h = bHeight2, c = 'import js_animPolish.js_stickyMod as js_stickyMod ; reload (js_stickyMod) ; js_stickyMod.addGeo_sel ()')
	cmds.button (l = 'Remove Geo', bgc = bColor_brown, ann = 'Remove selected geo from selected sticky mod.', w = (width/2), h = bHeight2, c = 'import js_animPolish.js_stickyMod as js_stickyMod ; reload (js_stickyMod) ; js_stickyMod.removeGeo_sel ()')
	cmds.button (l = 'Ori To World', bgc = bColor_brown, ann = 'Orient selected sticky mod to the world.', w = (width/2), h = bHeight2, c = 'import js_animPolish.js_stickyMod as js_stickyMod ; reload (js_stickyMod) ; js_stickyMod.oriToWorld_sel ()')
	cmds.button (l = 'Aim At Sel', bgc = bColor_brown, ann = "Select an object and a sticky mod to aim the sticky mod's null at the object.", w = (width/2), h = bHeight2, c = 'import js_animPolish.js_stickyMod as js_stickyMod ; reload (js_stickyMod) ; js_stickyMod.aimAtObj_sel ()')
	cmds.setParent ('..')
	cmds.button (l = 'Break Rivet Rotation', bgc = bColor_brown, ann = 'Break rotation follow on the null of the selected sticky mod.', h = bHeight2, c = 'import js_animPolish.js_stickyMod as js_stickyMod ; reload (js_stickyMod) ; js_stickyMod.breakRot_sel ()')
	cmds.separator (h = 6, style = 'double')
	cmds.rowColumnLayout (nc = 5, rs = [3,3], cs = [3,3])
	cmds.text (l = 'Falloff Radius:  ', ann = 'Default value for Falloff Radius.')
	cmds.floatField ('jsap_sm_falloff_ff', v = 1, pre = 2, w = 40, ann = 'Default value for Falloff Radius.')
	cmds.text (l = '  Smooth Map:  ', ann = "If running on multiple verts for auto-flooding, the map will be smoothed this number of times.")
	cmds.intField ('jsap_sm_smooth_if', v = 3, min = 0, w = 40, ann = "If running on multiple verts for auto-flooding, the map will be smoothed this number of times.")
	cmds.setParent ('..')
	cmds.separator (h = 1, style = 'none')
	cmds.rowColumnLayout (nc = 4, cs = ([2,3],[3,3],[4,3]))
	cmds.optionMenu ('jsap_sm_vis_om', l = 'Mode:', w = 139, ann = 'Choose whether default visualization mode is a Nurbs Curve or a Handle. Set your viewport display options accordingly.')
	cmds.menuItem ('jsap_sm_vis1_mi', l = 'Handle')
	cmds.menuItem ('jsap_sm_vis2_mi', l = 'Nurbs Curve')
	cmds.text (l = '  Crv Scale: ', ann = 'Size the nurbs curve control is built at. Ignore if you prefer Handle mode.')
	cmds.floatField ('jsap_sm_scale_ff', v = 1, pre = 2, min = .001, w = 40, ann = 'Size the nurbs curve control is built at. Ignore if you prefer Handle mode.')
	cmds.setParent ('..')
	cmds.separator (h = 1, style = 'none')
	cmds.rowColumnLayout (nc = 4, cs = ([2,3],[3,3],[4,3]))
	cmds.text (l = '  ')
	cmds.checkBox ('jsap_sm_sphere_cb', l = 'Sphere   ', v = 1, ann = 'Radius display spheres will be turned off by default.')
	cmds.checkBox ('jsap_sm_lra_cb', l = 'Axis   ', v = 0, ann = 'Local Rotation Axes will be turned on be default.')
	cmds.checkBox ('jsap_sm_forceDisplay_cb', l = 'Force Display', v = 1, ann = 'Turns on viewport display for relevant object types on creation.')
	cmds.setParent ('..')
	cmds.setParent ('..')
	cmds.separator (h = 1, st = 'none')
	cmds.setParent ('..')
	cmds.setParent ('..')

	"""
	# Sculpt Pose
	cmds.frameLayout ('jsap_sculptPose_fl', l = 'Sculpt Pose', cll = 1, cl = 0, mh = 8, mw = 15, w = width, ann = "Animate custom geo sculpts over time.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '                      Sculpt', i = 'putty.png', bgc = bColor_green, ann = 'Duplicate selected geo for sculpting.', st = 'iconAndTextHorizontal', w = bWidth, h = bHeight, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_sculpt ()')
	cmds.button (l = 'Sculpt From Zero', bgc = bColor_green, ann = 'Duplicate selected geo for sculpting, with all existing sculpt deformation removed.', w = bWidth, h = bHeight2, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload (js_animPolish_ui) ; js_animPolish_ui.scu_sculptFromZero ()')
	cmds.separator (h = 6, style = 'double')
	cmds.iconTextButton (l = '               Apply Standard', bgc = bColor_blue, i = 'nurbsToPolygons.png', st = 'iconAndTextHorizontal', ann = 'Apply selected sculpt as a standard shape.', h = bHeight, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_apply ()')
	cmds.button (l = 'Apply Standard 1-Frame', bgc = bColor_blue, ann = 'Apply selected sculpt mesh as a standard sculpt keyed 0-1-0 around current frame.', h = bHeight2, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_apply_1f ()')
	cmds.separator (h = 6, style = 'double')
	cmds.iconTextButton (l = '           Apply Pose-To-Pose', bgc = bColor_purple, i = 'setKeyOnAnim.png', st = 'iconAndTextHorizontal', ann = 'Apply selected sculpt mesh as a Pose-To-Pose sculpt, automatically keying in and out of existing P2P shapes.', h = bHeight, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_apply_p2p ()')
	cmds.button (l = 'Create P2P Zero', bgc = bColor_purple, ann = 'Skipping the sculpt step, create a P2P sculpt with no sculpt deformation.', w = (bWidth/2), h = bHeight2, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_createP2PZero ()')
	cmds.button (l = 'Create P2P Hold', bgc = bColor_purple, ann = 'Skipping the sculpt step, create a P2P sculpt with the deformation of the previous P2P sculpt.', w = (bWidth/2), h = bHeight2, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_createP2PHold ()')
	cmds.separator (h = 6, style = 'double')
	cmds.rowColumnLayout (nc = 2, rs = [2,3], cs = [2,3])
	cmds.button (l = 'Delete CB Sel', bgc = bColor_red, ann = 'Deletes shapes and releated nodes based on channel box selection.', w = (bWidth/2), h = bHeight2, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_delete (allP2P = 0)')
	cmds.button (l = 'Delete All P2P', bgc = bColor_red, ann = 'Deletes entire Pose-To-Pose System.', w = (bWidth/2), h = bHeight2, c = "import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_delete (allP2P = 1)")
	cmds.setParent ('..')
	cmds.separator (h = 6, style = 'double')
	cmds.rowColumnLayout (nc = 2, rs = [2,3], cs = [2,3])
	cmds.button (l = 'Edit Sculpt', bgc = bColor_brown, ann = 'Start sculpting a sculpt that will be automatically driven by the selected sculpt in the channel box.', w = bWidth/2, h = bHeight2, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_editSculpt ()')
	cmds.button (l = 'Apply Edit', bgc = bColor_brown, ann = 'Apply the edited sculpt mesh.', w = bWidth/2, h = bHeight2, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.scu_applyEdit ()')
	cmds.setParent ('..')
	cmds.button (l = 'Sort Channel Box', bgc = bColor_brown, h = bHeight2, ann = "If you used undo after hitting one of the delete buttons, you may need to sort the channel box with this button.", c = "import js_animPolish.js_sculptPose as js_sculptPose ; reload (js_sculptPose) ; js_sculptPose.sortCB ()")
	cmds.separator (h = 6, style = 'double')
	cmds.rowColumnLayout (nc = 3, rs = [3,5], cs = [3,3])
	cmds.checkBox ('jsap_scuVis_cb', l = 'Vis Toggle  ', v = 1, ann = 'Automatically toggles visibility between original geo and duplicated sculpts.')
	cmds.checkBox ('jsap_scuReshade_cb', l = 'Re-Shade ', v = 1, ann = 'Applies a shiny blue shader to duplicated sculpt geo so they are easily recognized.')
	cmds.checkBox ('jsap_scuData_cb', l = 'Hide Data', v = 1, ann = 'Prevents data nodes from cluttering up the outliner, channel box, and attribute editor. You can still find them through the node editor.')
	cmds.setParent ('..')
	cmds.separator (h = 1, style = 'none')
	cmds.rowColumnLayout (nc = 3, rs = [3,3], cs = [3,3])
	cmds.text (l = 'P2P Level: ', ann = 'When creating P2P sculpts, the automatic keyframing process will only be affected by P2P sculpts of the same level.')
	cmds.intField ('jsap_scuLevel_if', v = 1, min = 1, w = 40, ann = 'When creating P2P sculpts, the automatic keyframing process will only be affected by P2P sculpts of the same level.')
	cmds.optionMenu ('jsap_sfz_om', l = '   SFZ:', w = 145, ann = 'Choose which sculpts get zeroed out when using Sculpt From Zero.')
	cmds.menuItem ('jsap_sfz1_mi', l = 'All Sculpts')
	cmds.menuItem ('jsap_sfz2_mi', l = 'Standard')
	cmds.menuItem ('jsap_sfz3_mi', l = 'P2P')
	cmds.menuItem ('jsap_sfz4_mi', l = 'Current P2P Level')
	cmds.setParent ('..')
	cmds.separator (h = 6, st = 'none')
	cmds.setParent ('..')
	cmds.setParent ('..')

	# Wrap++
	cmds.frameLayout ('jsap_wrap_fl', l = 'Wrap ++', cll = 1, cl = 0, mh = 8, mw = 15, w = width, ann = "Wrap geo to other meshes, or lock them in space.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '                Wrap To Mesh', i = 'wrap.png', bgc = bColor_green, ann = 'Utilizing paintable blend shapes, wraps duplicates of meshes in selection to the last mesh in selection.', st = 'iconAndTextHorizontal', h = bHeight, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.wrap_wrapToMesh ()')
	cmds.iconTextButton (l = '               Wrap To World', i = 'duplicateCurve.png', bgc = bColor_green, ann = 'Blends duplicates of selected objects frozen in space back to their respective originals.', st = 'iconAndTextHorizontal', h = bHeight, c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.wrap_wrapToWorld ()')
	cmds.iconTextButton (l = '         Extract Animated Faces', i = 'polyChipOff.png', bgc = bColor_brown, ann = "Duplicates selected faces with animation in-tact. Useful for creating simple surfaces to wrap geo to with the 'Wrap' tool.", st = 'iconAndTextHorizontal', w = bWidth, h = bHeight, c = 'import js_animPolish.js_wrap as js_wrap ; reload (js_wrap) ; js_wrap.extractFaces ()')
	cmds.separator (h = 6, style = 'double')
	cmds.rowColumnLayout (nc = 6, rs = [4,3], cs = [4,3])
	cmds.text (l = 'Flood Verts:  ')
	cmds.textField ('jsap_wrap_autoFlood_tf', w = 95, ann = "If this field is filled, any non-loaded verts will be flooded to zero.")
	cmds.text (l = '', w = 1)
	cmds.button (l = 'Load', ann = "Loads selected verts. If the field is filled, any non-loaded verts will be flooded to zero.", c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.wrap_loadVerts ()')
	cmds.text (l = '', w = 3)
	cmds.button (l = 'Clear', ann = "Clears loaded verts.", c = 'import js_animPolish.js_animPolish_ui as js_animPolish_ui ; reload(js_animPolish_ui) ; js_animPolish_ui.wrap_clearVerts ()')
	cmds.setParent ('..')
	cmds.separator (h = 1, style = 'none')
	cmds.rowColumnLayout (nc = 4, rs = [2,3], cs = [2,3])
	cmds.text (l = '                       Smooth Map: ', ann = "If flooding verts, the map will be smoothed this number of times.")
	cmds.intField ('jsap_wrap_autoSmooth_if', v = 3, min = 0, w = 35, ann = "If flooding verts, the map will be smoothed this number of times.")
	cmds.text (l = '    ')
	#cmds.checkBox ('jsap_wrap_data_cb', l = 'Hide Data', v = 1, ann = 'Prevents data nodes from cluttering up the outliner, channel box, and attribute editor. You can still find them through the node editor.')
	cmds.setParent ('..')
	cmds.separator (h = 6, st = 'none')
	cmds.setParent ('..')
	cmds.setParent ('..')

	# Subdue
	cmds.frameLayout ('jsap_subdue_fl', l = 'Subdue', cll = 1, cl = 1, mh = 8, mw = 15, w = width, ann = "Softens vertex motion over time.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '     Unlock AnimPolish PREMIUM!', i = 'animateSnapshot.png', bgc = bColor_green, st = 'iconAndTextHorizontal', ann = "Unlock access to the full set of AnimPolish tools!", h = bHeight+10, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish')")
	cmds.setParent ('..')
	cmds.setParent ('..')

	# Misc. Deformation
	cmds.frameLayout ('jsap_miscDeformation_fl', l = 'Misc. Deformation', cll = 1, cl = 1, mh = 8, mw = 15, w = width, ann = "Simple deformation tools for growing/shrinking and smoothing.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '     Unlock AnimPolish PREMIUM!', i = 'animateSnapshot.png', bgc = bColor_green, st = 'iconAndTextHorizontal', ann = "Unlock access to the full set of AnimPolish tools!", h = bHeight+10, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish')")
	cmds.setParent ('..')
	cmds.setParent ('..')

	# Native Maya
	cmds.frameLayout ('jsap_nativeMaya_fl', l = 'Native Maya', cll = 1, cl = 1, mh = 8, mw = 15, w = width, ann = "Built-in Maya deformers useful for tech anim.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '     Unlock AnimPolish PREMIUM!', i = 'animateSnapshot.png', bgc = bColor_green, st = 'iconAndTextHorizontal', ann = "Unlock access to the full set of AnimPolish tools!", h = bHeight+10, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish')")
	cmds.setParent ('..')
	cmds.setParent ('..')

	# Assign Colors
	cmds.frameLayout ('jsap_assignColors_fl', l = 'Assign Colors', cll = 1, cl = 1, mh = 8, mw = 15, w = width, ann = "Assign lambert and blinn materials of common colors to objects for easy spotting of inter-penetrations, either manually or randomly.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '     Unlock AnimPolish PREMIUM!', i = 'animateSnapshot.png', bgc = bColor_green, st = 'iconAndTextHorizontal', ann = "Unlock access to the full set of AnimPolish tools!", h = bHeight+10, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish')")
	cmds.setParent ('..')
	cmds.setParent ('..')

	# Utilities
	cmds.frameLayout ('jsap_utilities_fl', l = 'Utilities', cll = 1, cl = 1, mh = 8, mw = 15, w = width, ann = "Random helpers for various tasks.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '     Unlock AnimPolish PREMIUM!', i = 'animateSnapshot.png', bgc = bColor_green, st = 'iconAndTextHorizontal', ann = "Unlock access to the full set of AnimPolish tools!", h = bHeight+10, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish')")
	cmds.setParent ('..')
	cmds.setParent ('..')

	# Caching
	cmds.frameLayout ('jsap_caching_fl', l = 'Caching', cll = 1, cl = 1, mh = 8, mw = 15, w = width, ann = "Export alembic caches into their own lightweight scenes for a fast workflow.")
	cmds.columnLayout (adj = 1, rs = 3)
	cmds.iconTextButton (l = '     Unlock AnimPolish PREMIUM!', i = 'animateSnapshot.png', bgc = bColor_green, st = 'iconAndTextHorizontal', ann = "Unlock access to the full set of AnimPolish tools!", h = bHeight+10, c = "import webbrowser ; webbrowser.open('http://joshsobelrigs.com/animpolish')")
	cmds.separator (h = 6, st = 'none')
	cmds.setParent ('..')
"""
	# Launch
	cmds.showWindow (win)
	cmds.window (win, e = 1, w = width+20, h = height)

	# Dock
	if dock == 1:
		cmds.dockControl (dockUI, l = 'AnimPolish', area = 'right', content = win, allowedArea = ['right', 'left'])
		cmds.refresh ()
		cmds.dockControl (dockUI, e = 1, r = 1, w = width+20)

"""
	# Refresh fields
	loadSettings ()
"""



########################
### Sticky Mod Funcs ###
########################



def sm_create ():

	sphVis = cmds.checkBox ('jsap_sm_sphere_cb', q = 1, v = 1)
	lra = cmds.checkBox ('jsap_sm_lra_cb', q = 1, v = 1)
	falloff = cmds.floatField ('jsap_sm_falloff_ff', q = 1, v = 1)
	smooth = cmds.intField ('jsap_sm_smooth_if', q = 1, v = 1)
	mode = cmds.optionMenu ('jsap_sm_vis_om', q = 1, sl = 1)
	scale = cmds.floatField ('jsap_sm_scale_ff', q = 1, v = 1)
	display = cmds.checkBox ('jsap_sm_forceDisplay_cb', q = 1, v = 1)
	js_stickyMod.run_sel (falloff = falloff, sphVis = sphVis, smooth = smooth, lra = lra, mode = mode, scale = scale)
	if display == 1:
		try:
			panel = cmds.getPanel (wf = 1)
			cmds.modelEditor (panel, e = 1, nurbsCurves = 1)
			if mode == 1 or lra == 1:
				cmds.modelEditor (panel, e = 1, handles = 1)
		except:
			try:
				cmds.modelEditor ('modelPanel4', e = 1, nurbsCurves = 1)
				if mode == 1 or lra == 1:
					cmds.modelEditor ('modelPanel4', e = 1, handles = 1)
			except:
				sys.stdout.write ("Sticky Mod created! However, relevant viewport display options were not enabled because a viewport was not found.")


#########################
### Sculptimate Funcs ###
#########################



def scu_sculpt ():

	vis = cmds.checkBox ('jsap_scuVis_cb', q = 1, v = 1)
	shade = cmds.checkBox ('jsap_scuReshade_cb', q = 1, v = 1)
	js_sculptPose.sculpt_sel (vis = vis, shade = shade)

def scu_sculptFromZero ():

	mode = cmds.optionMenu ('jsap_sfz_om', q = 1, sl = 1)
	vis = cmds.checkBox ('jsap_scuVis_cb', q = 1, v = 1)
	shade = cmds.checkBox ('jsap_scuReshade_cb', q = 1, v = 1)
	lv = cmds.intField ('jsap_scuLevel_if', q = 1, v = 1)
	js_sculptPose.sculptFromZero_sel (vis = vis, shade = shade, lv = lv, mode = mode)

def scu_apply ():

	ihi = cmds.checkBox ('jsap_scuData_cb', q = 1, v = 1)
	lv = cmds.intField ('jsap_scuLevel_if', q = 1, v = 1)
	js_sculptPose.apply_sel ('standard', lv = lv, ihi = ihi)

def scu_apply_1f ():

	js_sculptPose.apply_1f_sel ()

def scu_apply_p2p ():

	lv = cmds.intField ('jsap_scuLevel_if', q = 1, v = 1)
	ihi = cmds.checkBox ('jsap_scuData_cb', q = 1, v = 1)
	js_sculptPose.apply_p2p_sel (lv = lv, ihi = ihi)

def scu_createP2PZero ():

	lv = cmds.intField ('jsap_scuLevel_if', q = 1, v = 1)
	js_sculptPose.createP2PZero_sel (lv)

def scu_createP2PHold ():

	lv = cmds.intField ('jsap_scuLevel_if', q = 1, v = 1)
	ihi = cmds.checkBox ('jsap_scuData_cb', q = 1, v = 1)
	js_sculptPose.createP2PHold_sel (lv = lv, ihi = ihi)

def scu_delete (allP2P = 0):

	lv = cmds.intField ('jsap_scuLevel_if', q = 1, v = 1)
	js_sculptPose.delete_sel (lv, allP2P = allP2P)

def scu_editSculpt ():

	vis = cmds.checkBox ('jsap_scuVis_cb', q = 1, v = 1)
	shade = cmds.checkBox ('jsap_scuReshade_cb', q = 1, v = 1)
	js_sculptPose.editSculpt_sel (vis = 1, shade = 1)

def scu_applyEdit ():

	vis = cmds.checkBox ('jsap_scuVis_cb', q = 1, v = 1)
	shade = cmds.checkBox ('jsap_scuReshade_cb', q = 1, v = 1)
	lv = cmds.intField ('jsap_scuLevel_if', q = 1, v = 1)
	ihi = cmds.checkBox ('jsap_scuData_cb', q = 1, v = 1)
	js_sculptPose.applyEdit_sel (lv = lv, ihi = ihi)



#####################
### Wrap ++ Funcs ###
#####################



def wrap_loadVerts ():

	sel = cmds.ls (sl = 1, fl = 1)
	verts = []
	for i in sel:
		verts.append (str(i))
	cmds.textField ('jsap_wrap_autoFlood_tf', e = 1, tx = str(verts))

def wrap_clearVerts ():

	cmds.textField ('jsap_wrap_autoFlood_tf', e = 1, tx = '')

def wrap_wrapToMesh ():

	verts = cmds.textField ('jsap_wrap_autoFlood_tf', q = 1, tx = 1)
	smooth = cmds.intField ('jsap_wrap_autoSmooth_if', q = 1, v = 1)
	#hideData = cmds.checkBox ('jsap_wrap_data_cb', q = 1, v = 1)
	#js_wrap.wrapToMesh_sel (verts = verts, smooth = smooth, hideData = hideData)
	js_wrap.wrapToMesh_sel (verts = verts, smooth = smooth)

def wrap_wrapToWorld ():

	verts = cmds.textField ('jsap_wrap_autoFlood_tf', q = 1, tx = 1)
	smooth = cmds.intField ('jsap_wrap_autoSmooth_if', q = 1, v = 1)
	#hideData = cmds.checkBox ('jsap_wrap_data_cb', q = 1, v = 1)
	#js_wrap.wrapToWorld_sel (verts = verts, smooth = smooth, hideData = hideData)
	js_wrap.wrapToWorld_sel (verts = verts, smooth = smooth)



#################
### Utilities ###
#################



def saveSettings_run (typ, name, flag, f):

	exec ("val = cmds.{} ('{}', q = 1, {} = 1)".format (typ,name,flag))
	if typ == 'radioCollection':
		cmd = "        cmds.{} ('{}', e = 1, {} = '{}')\n".format (typ,name,flag,val)
	else:
		cmd = "        cmds.{} ('{}', e = 1, {} = {})\n".format (typ,name,flag,val)
	f.write (cmd)

def saveSettings ():

	# Get path
	root = jsap.__file__
	root = root.replace ('__init__.py', '')
	path = '{}user_settings.py'.format (root)
	f = open (path, 'w')
	f.write ("import maya.cmds as cmds\n\n")
	f.write ("def run ():\n\n")

	# Sticky Mod
	f.write ('    # Sticky Mod\n')
	f.write ('    try:\n')
	saveSettings_run ('frameLayout', 'jsap_stickyMod_fl', 'cl', f)
	saveSettings_run ('floatField', 'jsap_sm_falloff_ff', 'v', f)
	saveSettings_run ('intField', 'jsap_sm_smooth_if', 'v', f)
	saveSettings_run ('optionMenu', 'jsap_sm_vis_om', 'sl', f)
	saveSettings_run ('floatField', 'jsap_sm_scale_ff', 'v', f)
	saveSettings_run ('checkBox', 'jsap_sm_sphere_cb', 'v', f)
	saveSettings_run ('checkBox', 'jsap_sm_lra_cb', 'v', f)
	saveSettings_run ('checkBox', 'jsap_sm_forceDisplay_cb', 'v', f)
	f.write ('    except:\n')
	f.write ('        pass\n')
	f.write ('\n')
	
	# Sculpt Pose
	f.write ('    # Sculpt Pose\n')
	f.write ('    try:\n')
	saveSettings_run ('frameLayout', 'jsap_sculptPose_fl', 'cl', f)
	saveSettings_run ('checkBox', 'jsap_scuVis_cb', 'v', f)
	saveSettings_run ('checkBox', 'jsap_scuReshade_cb', 'v', f)
	saveSettings_run ('checkBox', 'jsap_scuData_cb', 'v', f)
	saveSettings_run ('intField', 'jsap_scuLevel_if', 'v', f)
	saveSettings_run ('optionMenu', 'jsap_sfz_om', 'sl', f)
	f.write ('    except:\n')
	f.write ('        pass\n')
	f.write ('\n')

	# Wrap ++
	f.write ('    # Wrap ++\n')
	f.write ('    try:\n')
	saveSettings_run ('frameLayout', 'jsap_wrap_fl', 'cl', f)
	saveSettings_run ('intField', 'jsap_wrap_autoSmooth_if', 'v', f)
	f.write ('    except:\n')
	f.write ('        pass\n')
	f.write ('\n')

	# Close
	f.close ()

def loadSettings ():

	try:
		import js_animPolish.user_settings as user_settings
		reload (user_settings)
		user_settings.run ()
	except:
		try:
			import js_animPolish.user_settings_default as user_settings_default
			reload (user_settings_default)
			user_settings_default.run ()
		except:
			sys.stdout.write ("Failed to load custom settings. Using defaults.")

def defaultSettings ():

	root = jsap.__file__
	root = root.replace ('__init__.py', '')
	path = '{}user_settings.py'.format (root)
	try:
		os.remove (path)
	except:
		pass
	loadSettings ()

def toggleAnimEval ():

	rslt = toggleAnimEval_2 ()
	cmds.refresh ()
	sys.stdout.write ("Switched animation evaluation mode to '{}'.".format (rslt))
	cmds.refresh ()

def toggleAnimEval_2 ():

	mode = cmds.evaluationManager (q = 1, mode = 1)[0]
	if mode == 'off':
		cmds.evaluationManager (e = 1, mode = 'parallel')
		rslt = 'Parallel'
	elif mode == 'parallel' or mode == 'serial':
		cmds.evaluationManager (e = 1, mode = 'off')
		rslt = 'DG'
	return rslt