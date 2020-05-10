$(document).ready(function () {
    var url = window.location.pathname;
    $(".nav_ul li").removeClass("this");
    if (url == "/") {
        $(".nav_ul li").eq(0).addClass("this")
    } else if (url == "/forum") {
        $(".nav_ul li").eq(1).addClass("this")
    } else if (url == "/member") {
        $(".nav_ul li").eq(2).addClass("this")
    }
    $(".player_full_screen").click(function () {
        if ($(".work-player").hasClass("full_screen")) {
            $(".work-player").removeClass("full_screen");
            $("html").css("overflow", "")
        } else {
            $(".work-player").addClass("full_screen");
            $("html").css("overflow", "hidden")
        }
    });
    $(".player_refresh").click(function () {
        $("#player").attr("src", $("#player").attr("src"))
    });
    if (document.readyState == "interactive") {
        $("#loading").css("display","none")
    }
})




