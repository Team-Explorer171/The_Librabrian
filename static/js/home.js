$("#nav-toggler").on("change", () => {
    var i = $("label[for='nav-toggler'] > i");
    i.addClass("rotate_x");
    setTimeout(() => {
        i.removeAttr("class").addClass(
            `fas fa-${$("#nav-toggler").prop("checked") ? "times" : "bars"} rotate_b`
        );
    }, 400);
    setTimeout(() => {
        i.removeClass("rotate_b");
    }, 810);
});
