(function (i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r;
    i[r] = i[r] || function () {
        (i[r].q = i[r].q || []).push(arguments)
    }, i[r].l = 1 * new Date();
    a = s.createElement(o), m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m)
})(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
ga('create', 'UA-120909275-1', 'auto');
ga('send', 'pageview');
$("body").on("contextmenu", function (e) {
    return false;
});
$(document).keydown(function (e) {
    if (e.ctrlKey && (e.keyCode === 67 || e.keyCode === 86 || e.keyCode === 85 || e.keyCode === 117)) {
        return false;
    }
    if (e.which === 123) {
        return false;
    }
    if (e.metaKey) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 73) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 74) {
        return false;
    }
    if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
        return false;
    }
    if (e.keyCode == 224 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 85) {
        return false;
    }
    if (event.keyCode == 123) {
        return false;
    }
});
(function ($) {
    "use strict";
    $('.minus').click(function () {
        var $input = $(this).parent().find('.box');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('.box');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });
    var $main_nav = $('#main-nav');
    var $toggle = $('.toggle');
    var defaultOptions = {
        disableAt: false,
        customToggle: $toggle,
        levelSpacing: 40,
        navTitle: 'App',
        levelTitles: true,
        levelTitleAsBack: true,
        pushContent: '#container',
        insertClose: 2
    };
    var Nav = $main_nav.hcOffcanvasNav(defaultOptions);
    $('.coupons').slick({infinite: false, arrows: false, autoplay: true, slidesToShow: 1.3, slidesToScroll: 1,});
    $('.top-picks').slick({infinite: false, arrows: false, autoplay: true, slidesToShow: 2.3, slidesToScroll: 1,});
    $('.all-cate').slick({infinite: false, arrows: false, autoplay: false, slidesToShow: 4.5, slidesToScroll: 4,});
    $('.product-slider').slick({arrows: false, autoplay: false, infinite: false, dots: true,});
})(jQuery);