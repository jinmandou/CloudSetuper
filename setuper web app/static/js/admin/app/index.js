define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var log = require('log');
    var util = require('app/util');
    var logout = require('../app/logout');
    $(function(){
        log('index');
        logout.logout();
    });
});
