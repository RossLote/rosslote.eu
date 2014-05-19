$(function() {
    $("img.js-hover-effect")
        .mouseover(function() {
            var oldSrc = $(this).attr("src");
            var ext = oldSrc.split('.').pop();
            var src = oldSrc.match(/[^\.]+/) + "_over." + ext;
            $(this).attr("src", src);
        })
        .mouseout(function() {
            var src = $(this).attr("src").replace("_over.", ".");
            $(this).attr("src", src);
        });
});
