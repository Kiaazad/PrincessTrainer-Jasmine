init python:
    config.keymap = dict(
        game_menu = [ 'K_ESCAPE', 'K_MENU', 'mouseup_3' ],
        screenshot = [ 'o', 'alt_K_s', 'alt_shift_K_s' ],
        toggle_fullscreen = ['alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11' ],
        hide_windows = [ 'mouseup_2', 'h' ],
        help = [ 'K_F1', 'meta_shift_/' ],

        # These keys control skipping.
        skip = [ 'K_LCTRL', 'K_RCTRL' ],
        stop_skipping = [ ],
        toggle_skip = [ 'K_TAB' ],
        fast_skip = [ '>' ],

        # Say.
        rollback = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ],
        rollforward = [ 'K_PAGEDOWN', 'repeat_K_PAGEDOWN', 'mousedown_5' ],
        dismiss = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ],
        dismiss_unfocused = [ ],

        # Focus.
        focus_left = [ 'K_LEFT', 'repeat_K_LEFT', 'a' ],
        focus_right = [ 'K_RIGHT', 'repeat_K_RIGHT', 'd' ],
        focus_up = [ 'K_UP', 'repeat_K_UP', 'w' ],
        focus_down = [ 'K_DOWN', 'repeat_K_DOWN', 's' ],

        # Bar.
        bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'e' ],
        bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'e' ],
        bar_left = [ 'K_LEFT', 'repeat_K_LEFT', 'a' ],
        bar_right = [ 'K_RIGHT', 'repeat_K_RIGHT', 'd' ],
        bar_up = [ 'K_UP', 'repeat_K_UP', 'w' ],
        bar_down = [ 'K_DOWN', 'repeat_K_DOWN', 's' ],

        # Button.
        button_ignore = [ 'mousedown_1' ],
        button_select = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'e' ],
        button_alternate = [ 'mouseup_3' ],
        button_alternate_ignore = [ 'mousedown_3' ],

        # Input.
        input_backspace = [ 'K_BACKSPACE', 'repeat_K_BACKSPACE' ],
        input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
        input_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
        input_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
        input_up = [ 'K_UP', 'repeat_K_UP' ],
        input_down = [ 'K_DOWN', 'repeat_K_DOWN' ],
        input_delete = [ 'K_DELETE', 'repeat_K_DELETE' ],
        input_home = [ 'K_HOME' ],
        input_end = [ 'K_END' ],
        input_copy = [ 'ctrl_K_INSERT', 'ctrl_K_c' ],
        input_paste = [ 'shift_K_INSERT', 'ctrl_K_v' ],


        # Accessibility.
        accessibility = [ "alt_K_a" ],
        self_voicing = [ 'v', 'V', 'alt_K_v'  ],
        clipboard_voicing = [ 'c', 'alt_shift_K_c' ],
        debug_voicing = [ 'alt_shift_K_v', 'meta_shift_K_v' ],

        # Pause.
        dismiss_hard_pause = [ ],

        # Viewport.
        viewport_leftarrow = [ 'K_LEFT', 'repeat_K_LEFT', 'a' ],
        viewport_rightarrow = [ 'K_RIGHT', 'repeat_K_RIGHT', 'd' ],
        viewport_uparrow = [ 'K_UP', 'repeat_K_UP', 'w' ],
        viewport_downarrow = [ 'K_DOWN', 'repeat_K_DOWN', 's' ],
        viewport_wheelup = [ 'mousedown_4' ],
        viewport_wheeldown = [ 'mousedown_5' ],
        viewport_drag_start = [ 'mousedown_1' ],
        viewport_drag_end = [ 'mouseup_1' ],
        viewport_pageup = [  'K_PAGEUP', 'repeat_K_PAGEUP' ],
        viewport_pagedown = [  'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],

        # Delete a save.
        save_delete = [ 'K_DELETE' ],

        # Draggable.
        drag_activate = [ 'mousedown_1' ],
        drag_deactivate = [ 'mouseup_1' ],

        # Debug console.
        console = [ 'shift_O', 'alt_shift_K_o' ],
        console_older = [ 'K_UP', 'repeat_K_UP' ],
        console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],

        # Ignored (kept for backwards compatibility).
        toggle_music = [ 'm' ],
        viewport_up = [ 'mousedown_4' ],
        viewport_down = [ 'mousedown_5' ],

        # Profile commands.
        performance = [ 'K_F3' ],
        image_load_log = [ 'K_F4' ],
        profile_once = [ 'K_F8' ],
        memory_profile = [ 'K_F7' ],

        # Director
        director = [ 'K_F8' ],

        # Developer
        developer = [ 'K_F9', 'alt_shift_K_d' ],
        full_inspector = [ 'alt_shift_K_i' ],
        inspector = [ 'I' ],
        reload_game = [ 'K_F5', 'alt_shift_K_r' ],
        launch_editor = [ 'E' ],
        choose_renderer = [ 'G', 'alt_shift_K_g' ],
        progress_screen = [ 'alt_shift_K_p', 'meta_shift_K_p', 'K_F2' ],

        dump_styles = [ ],
        toggle_afm = [ ],
        quit = [ ],
        iconify = [ ],
        )
