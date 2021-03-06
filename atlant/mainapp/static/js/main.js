$(window).on('load', function () {
    if (window.location.pathname.indexOf('/uz/') !== -1) {
        let path, new_path;
        path = window.location.pathname;
        new_path = path.replace('/uz/', '');
        $('#header_lang_uz').attr('href', path + window.location.search);
        $('#mob_header_lang_uz').attr('href', path + window.location.search);
        $('#header_lang_ru').attr('href', '/' + new_path + window.location.search);
        $('#mob_header_lang_ru').attr('href', '/' + new_path + window.location.search);
    }
    else {
        let path;
        path = window.location.pathname;
        $('#header_lang_ru').attr('href', path + window.location.search);
        $('#header_lang_uz').attr('href', '/uz' + path + window.location.search);
        $('#mob_header_lang_ru').attr('href', path + window.location.search);
        $('#mob_header_lang_uz').attr('href', '/uz' + path + window.location.search);
    }
});