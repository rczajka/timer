(function() {
    $(function() {
        var $cnt = $("#countdown");

        function get_until(state) {
            var now = new Date();
            var date_start = now.getTime();
            var date = new Date(date_start +
                (state["minutes"] * 60 + state["seconds"]) * 1000)
            return date;
        }

        function highlight_secs(secs) {
            if (secs <= 0) { 
                $cnt.addClass('expired'); 
                $cnt.removeClass('warning'); 
            } else if (secs < 60) {
                if (secs & 1)
                    $cnt.addClass('warning');
                else 
                    $cnt.removeClass('warning');
            }
        }

        function highlight(periods) {
            var secs = $.countdown.periodsToSeconds(periods);
            highlight_secs(secs);
        }

        function set_clock(state) {
            $cnt.countdown({
                until: get_until(state),
                format: "MS",
                onTick: highlight
            });
            if (state["state"] == "pause" || state["state"] == "reset")
                $cnt.countdown("pause");
            highlight_secs(state["minutes"] * 60 + state["seconds"]);
            first = false;
        }

        set_clock(state);

        var last_change = state["change_stamp"];

        var update_state = function(text) {
            var state = $.parseJSON(text);
            if (state["change_stamp"] <= last_change)
                return;
            if (state["state"] == "pause") {
                $cnt.countdown("pause");
            }
            else if (state["state"] == "resume") {
                $cnt.countdown("resume");
            }
            else
                location.reload();
            last_change = state["change_stamp"];
        };
        
        if (slug)
            var state_url = '/t/' + slug + '/state/';
        else
            var state_url = '/state/';
        var check_state = function() {
            $.ajax(state_url, {
                dataType: 'text',
                success: update_state
            });
        };

        window.setInterval(check_state, 1000);

    });
})(jQuery);
