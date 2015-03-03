var minlength = 3;
// initial interval value
var SearchTimeOut = 0;
// how long before the execution starts; in milliseconds (1000 = 1 second)
// just the value i'm happy with, not too fast or slow
// increase value if you think users type 1 ltr (letter per second) &gt;:)
var Interval = 777;
var sliderInterval = 10000;
var imagePath = "images/";

 
// stores the search keyword
var CurrentSearchKey = '';

var mouse_is_inside = false;

$(document).ready( function () {
	
	//Novo starts
	
	$("#event_reg_start").click(function(){
		eventReg();
	});
	
	//Novo ends

	//Calendar
	if ( $('.calendar-horizontal')[0] ) { 
		lth_calendar(); 
	}
	
	//Fancybox lightbox
	$('a.fancybox-enlarge').fancybox();
	
	$('a.fancybox-gallery').fancybox();
	
	$('.various').fancybox({
		maxWidth	: 800,
		maxHeight	: 600,
		fitToView	: false,
		width		: '70%',
		height		: '70%',
		autoSize	: false,
		closeClick	: false,
		openEffect	: 'none',
		closeEffect	: 'none'
	});
	
	$('a.promo_video, a.lightbox').click(function() {
		//alert(this.href);
		if(this.href.indexOf('www.youtube.com') > 0) {
		$.fancybox({
			'type' : 'iframe',
	        // hide the related video suggestions and autoplay the video
	        //'href' : this.href.replace(new RegExp('watch\\?v=', 'i'), 'embed/') + '?rel=0&autoplay=1',
			'href' : this.href + '?rel=0&autoplay=1',
	        'overlayShow' : true,
	        'centerOnScroll' : true,
	        'speedIn' : 100,
	        'speedOut' : 50,
	        'width' : 640,
	        'height' : 480
		});
		} else {
			$.fancybox({
			    'padding' : 10,
			    'autoScale' : false,
			    'title' : this.title,
			    'overlayOpacity' : '1.6',
			    'overlayColor' : '#333',
			    'transitionIn' : 'none',
			    'transitionOut' : 'none',
			    'centerOnScroll' : false,
			    'showCloseButton' : true,
			    'hideOnOverlayClick': false,
			    'content': '<embed src="typo3/contrib/flashmedia/flvplayer.swf?file='+(this.href.replace(new RegExp("watch\\?v=", "i"), "v/"))+'&amp;autostart=true&amp;fs=1" type="application/x-shockwave-flash" width="640" height="376" wmode="opaque" allowfullscreen="true" allowscriptaccess="always"></embed>'
			});	
		}
		return false;
	});
	
	$(".fancybox").fancybox({
		openEffect	: 'none',
		closeEffect	: 'none'
	});
	
	//Main navigation with mega menu
	//$('.main-nav-inner-border').corner();
	$(function() {
		var $menu = $('#main-nav-menu');
		$menu.children('li').each(function(){
			var $this = $(this);
			//var $span = $this.children('span');
			//$span.data('width',$span.width());
			$this.bind('mouseenter',function(){
				if ( $this.find('span').length ) { 
					var pos = $this.find('span').position().left;
				}
				//var width = $this.find('span').width();
				$('.main-nav-arrow-up').css('backgroundPosition', pos + 10);
				$menu.find('.main-nav-submenu').stop(true,true).hide();
				//$span.stop().animate(300,function(){
				$this.find('.main-nav-submenu').slideDown(300);
				//});
			}).bind('mouseleave',function(){
				$this.find('.main-nav-submenu').stop(true,true).hide();
				//$span.stop().animate(300);
			});
		});
		//==##
		if($('.main-nav-inner-content-left').length){
		$('#newContactContent').siblings(".main-nav-inner-content-left").replaceWith($("#newContactContent").css('visibility','visible')); 
	}     
		//==##
		//============================================================= 
// "expand-div" function mainly for FAQ page 
// MP 2013/12/20
//=============================================================
$(".expandHeader").click(function () {
    $expandHeader = $(this);
    //getting the next element
    $expandContent = $expandHeader.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    $expandContent.slideToggle(500, function () {
    //replace bg-img if content is visible  
    $expandContent.is(":visible") ? $expandHeader.css("background-image", "url(/fileadmin/templates/images/arrowSmallDown.png)") : $expandHeader.css("background-image", "url(/fileadmin/templates/images/arrowSmall15.png)");
    });
});
	});
	
	//Login
	$('#login-flyout').click(function() {
		var loginBox = $('#login_box');
		console.log('221');
        if (loginBox.is(":visible")) {
            loginBox.fadeOut("fast");
        } else {
        	$.ajax({
        		type: "POST",
        		url: "index.php",
        		data: {
        			'eID' : 'lth',
        			'action' : 'getLoginBox',
        			'sid' : Math.random()
        		},
        		//contentType: "application/json; charset=utf-8",
        		dataType: "json",
        		beforeSend: function() {
        			$('#login_box_content').html('<img src="/fileadmin/templates/images/ajax-loader.gif" />');
				},
        		complete: function(data) {
        			$('#login_box_content').html(data.responseText);
        			//console.log('complete'+data.responseText);
        		},
        		failure: function(errMsg) {
        			console.log(errMsg);
        		}
        	});	
            loginBox.fadeIn("slow");
        }
        return false;
    });
	
	$("#login_box").hover(function(){ 
        mouse_is_inside=true; 
    }, function(){ 
        mouse_is_inside=false; 
    });

    $("body").click(function(){
       if(! mouse_is_inside) $("#login_box").fadeOut("fast");
    });
	
	$(".content-wrapper .text-content .content-navigation .menu-level-1 li").hover(function(){
	    $(this).css({backgroundColor: "#f1ede2"});
	}, function(){
	    $(this).css({backgroundColor: ""});
	});
	
	if ( $('#getSinglePid')[0] ) {
		//http://www.lth.se/nyheter-och-press/nyheter/visa-nyhet/article/lastcykel-foer-flexibelt-behov-1/
		var singleNewsLink = decodeURIComponent($('#getSinglePid a').attr('href'));
		var singleNewsLinkArray = singleNewsLink.split('/');
		var arrayCount = singleNewsLinkArray.length;
		if (arrayCount >= 4){
		singleNewsLinkArray.remove((arrayCount - 4),arrayCount);
		}
		//singleNewsLinkArray = singleNewsLinkArray[1].split('&');
		singleNewsLink = singleNewsLinkArray.join('/');
		//console.log("singlenewslink"+singleNewsLink);
		if ( $('#getGoToArchive').length ) {
		singleNewsLink = decodeURIComponent($('#getGoToArchive').attr('href'));
		}
		$('.archive_link a').attr('href',singleNewsLink);
	}
		
	//footer_logo
	//$('#footer_logo').attr('href','onclitypo3/index.php?redirect_url='+window.location.pathname);
	/*
	* TYPO3-login removed from logo and put in separate link MP 2014/01/28
	*/
	//Tror #footer_logo_en är gammalt, nu använder vi en_lu/en_lth 2015-01-29
	$("#footer_logo_en").click(function() {
	  window.location = '#';
	  //window.location = '/typo3/index.php?redirect_url='+window.location.pathname;
	});
	$("#footer_logo_en_lu").click(function() {
	   window.location = 'http://www.lunduniversity.lu.se/';
	});
	$("#footer_logo").click(function() {
	  window.location = 'http://www.lth.se';
	});
	$("#footer_logo_en_lth").click(function() {
	  window.location = 'http://www.lth.se/english';
	});
	$("#footer_logo_lu").click(function() {
	  window.location = 'http://www.lu.se/';
	});
	$(".header_logo_en_lth").attr("href","http://www.lth.se/english");
	$(".header_logo_lth").attr("href","http://www.lth.se");
	$(".header_logo").attr("href","http://www.lu.se");
	$(".header_logo_en").attr("href","http://www.lunduniversity.lu.se/");
	//lagt till +location.search för att få med query string, redirecten skickade inte med query string och fungerade därför inte alltid MP 2014-09-17
	$("#typo3Login").attr("href","/typo3/index.php?redirect_url="+window.location.pathname+location.search);
});

Array.prototype.remove = function(from, to)
{
	var rest = this.slice((to || from) + 1 || this.length);
	this.length = from < 0 ? this.length + from : from;
	return this.push.apply(this, rest);
};

function validateLink(link)
{
	if(isNormalInteger(link)) {
		window.location = 'index.php?id='+link;
	} else {
		window.location.href = link;
		//console.log(link);
		
	}
}

function inlinePresentation(e) {
	var temp = e.target;
	var elementName= temp.innerHTML;
	alert(elementName);
	 
    /*$("#elementName").click(function(){
		eventReg();
	});*/
	
}

function isNormalInteger(str) {
    return /^\+?(0|[1-9]\d*)$/.test(str);
}

function lth_calendar()
{
	$.ajax({
		type: "POST",
		url: "index.php",
		data: {
			eID : 'lth_calendar',
			sid : Math.random()
		},
		//contentType: "application/json; charset=utf-8",
		dataType: "json",
		beforeSend: function(){
			$('.calendar-horizontal').html('<img src="/typo3conf/ext/lth_calendar/res/ajax-loader.gif" />');
		},
		success: function(data) {
			//alert(data);
			//document.getElementById('calendar-horizontal').innerHTML = utf8_decode(data);
		},
		complete: function(data) {
			//alert(data.responseText);
			//document.write(data.responseText);
			//$('.calendar-horizontal').html(data.responseText);
			document.getElementById('calendar-horizontal').innerHTML = utf8_decode(data.responseText);
			//if(data[1]) $('#page_title').children().html(_decode(data[1]));
			//console.log(data);
		},
		failure: function(errMsg) {
			console.log(errMsg);
		}
	});
	
}

function eventReg()
{
	if (0 === $('.event-reg-modal-overlay').length) {
		var overlay = $('<div/>', {
			'class': 'event-reg-modal-overlay'
		}).appendTo('body');
	}
	
	if (0 === $('.event-reg-modal-window').length) {
		//var modal = $('body').append('<div class="feedit3-modal-window"></div>');
		var modal = $('<div/>', {
			'class': 'event-reg-modal-window'
		}).appendTo('body');
	}
	
	if (0 === $('.event-reg-container').length) {
		$('<div/>', {
			'class': 'event-reg-container'
		}).appendTo('.event-reg-modal-window');
	} else {
		$('.event-reg-container').html('');
	}
	
	$('<div/>', {
		'id': 'event-reg-content-wide',
		'class': 'event-reg-content-wide',
	}).appendTo('.event-reg-container');
	
	$('<div/>', {
		'class': 'event-reg-close',
		'html': '<button class="close">&times;</button>'
	}).appendTo('.event-reg-container');
	
	$('.close').click(function () {
		removeOverlay();
	});
	
	$.ajax({
		type: "POST",
		url: "index.php",
		data: {
			'eID' : 'tx_lthmailformadmin',
			'action' : 'formShow',
			'sid' : Math.random()
		},
		//contentType: "application/json; charset=utf-8",
		dataType: "json",
		beforeSend: function() {
			$('#event-reg-content-wide').html('<img src="/fileadmin/templates/images/ajax-loader.gif" />');
		},
		complete: function(data) {
			//console.log(data);
			$('#event-reg-content-wide').html(data.responseText);
			if(data) console.log('complete'+data.responseText);
		},
		/*success: function(data) {
			if(data) console.log('success'+data.responseText);
		},*/
		failure: function(errMsg) {
			console.log(errMsg);
		}
	});	
}

function ods_ajaxfelogin(obj)
{
	var prefix=obj.form.id.substr(0,obj.form.id.length-5);
	var content = '';
	//jQuery('#'+prefix+'_indication').css('display','block');
	//alert(obj.form.action.replace('http','https'));
	jQuery.ajax({  
		type: 'POST',  
		url: obj.form.action,  
		data: jQuery.param(jQuery(obj.form).serializeArray())+'&'+obj.name+'=1&tx_felogin_pi1[ajax]='+prefix,  
		success: function(data) {
			
			var response=jQuery.parseJSON(data);
			if(response.redirect) {
				//window.location.href=response.redirect;
			} else {
				//jQuery('#'+prefix).html(response.data);
				//jQuery('#'+prefix+'_indication').css('display','none');
				if(response.data.indexOf('success')>0) {
					content = 'Login succeded';
					$('#login-flyout').html('<i class=\"icon-user\"></i> Inloggad som&nbsp;'+getFeUser());
					$('#login-flyout').append('<li><a href="/logout?logintype=logout">Logga ut</a></li>');
				} else {
					content = 'Login failed';
				}
				$('#login_box_content').html(response.data);
			}
		},
		failure: function(errMsg) {
			console.log(errMsg);
		}
	});  
	return false;
}

function getFeUser()
{
	var content = '';
	
	$.ajax({
		type: "POST",
		url: "index.php",
		data: {
			'eID' : 'lth',
			'action' : 'getFeUser',
			'sid' : Math.random()
		},
		//contentType: "application/json; charset=utf-8",
		dataType: "json",
		complete: function(data) {
			//$('#login_box_content').html(data.responseText);
			content = data.responseText;
		},
		failure: function(errMsg) {
			console.log(errMsg);
		}
	});
	
	return content;
}

function autoGrowField(f, max)
{
   /* Default max height */
   var max = (typeof max == 'undefined')?1000:max;
   /* Don't let it grow over the max height */
   if (f.scrollHeight > max) {
      /* Add the scrollbar back and bail */
      if (f.style.overflowY != 'scroll') { f.style.overflowY = 'scroll'; }
      return;
   }
   /* Make sure element does not have scroll bar to prevent jumpy-ness */
   if (f.style.overflowY != 'hidden') { f.style.overflowY = 'hidden'; }
   /* Now adjust the height */
   var scrollH = f.scrollHeight;
   if( scrollH > f.style.height.replace(/[^0-9]/g,'') ){
      f.style.height = scrollH+'px';
   }
}

// cancels the previous search interval
var ResetSearch = function()
{
	// this is what cancels the setTimeout interval assigned
	// to SearchTimeOut
	clearTimeout(SearchTimeOut);
	SearchTimeOut = 0;
};

function createHamburgerNav()
{
    var pid;
    var ulCount=1;
    var liCount=1;
    var ii=0;
    var i=0;
    var selectedClass='';
    var selectedFlag=false;
    var content='';
    var oldLevel=0;
    var syslang = $('#syslanguageforMenu').val();
    var title;
    
    if(syslang>0) {
        HA = HA.filter(function(menuitem) { return menuitem.level < 7 && menuitem.label_ol!=''});
    } else {
        HA = HA.filter(function(menuitem) { return menuitem.level < 7});
    }

    $.each(HA, function(key, value) {
        if(value.uid==$('#pageUidforMenu').val()) {
            selectedClass=' selected';
            selectedFlag=true;
        } else {
            selectedClass='';
        }
        //console.log(value.label);
        if(syslang>0) {
            title = value.label_ol;
        } else {
            title = value.label;
        }      
         if(value.level<oldLevel) {
            i=0;
            for(i==0;i<=(ulCount-value.level);i++) {
                content += '</ul></li>';
                ulCount--;
            }
        }
        if(value.hassub>0){
            content += '<li class="has_sub'+selectedClass+'">'+'<a href="index.php/?id='+value.uid+'&L='+syslang+'">'+title+'</a><a class="responsive_link expand"></a>';
            content += '<ul class="menu-level-'+(value.level+1)+'">';
            ulCount++;
        } else {
            content += '<li class="'+selectedClass+'">'+'<a href="index.php/?id='+value.uid+'&L='+syslang+'">'+title+'</a></li>';
        }
        
        oldLevel = value.level;
        ii++;
    });
    if(selectedFlag===false) {
        selectedClass = ' selected';
    }
    
    i=0;
    for(i==0;i<=(ulCount-oldLevel);i++) {
        content += '</ul></li>';
    }
                
    content = '<ul class="menu-level-1"><li class="'+selectedClass+'"><a href="/">Start</a></li>'+content+'</ul>';

    $('#responsive_menu').after(content);
    
    //Expand - minimize the menu options
    $('#responsive_navigation .has_sub .responsive_link').click(function() {
      $(this).parent('.has_sub').toggleClass('expanded');
      $(this).siblings('ul').slideToggle(150);
      if ($(this).hasClass('expand')) {
        $(this).removeClass('expand').addClass('minimize');
      } else {
        $(this).removeClass('minimize').addClass('expand');
      }
    });

    //Expand menu options to the selected level on page load
      $('#responsive_navigation li.selected').each(function() {
      $(this).parents('#responsive_navigation ul').show();
      $(this).parents('.has_sub').addClass('expanded');
      $(this).children('ul').first().show();
      $(this).children('.responsive_link').removeClass('expand').addClass('minimize');
      $(this).parents('ul').siblings('.responsive_link').removeClass('expand').addClass('minimize');
    });
}

function debug(input)
{
	$('#debug').append('- ' + input + '<br />');
}

function utf8_decode (str_data) {
	  // http://kevin.vanzonneveld.net
	  // +   original by: Webtoolkit.info (http://www.webtoolkit.info/)
	  // +      input by: Aman Gupta
	  // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
	  // +   improved by: Norman "zEh" Fuchs
	  // +   bugfixed by: hitwork
	  // +   bugfixed by: Onno Marsman
	  // +      input by: Brett Zamir (http://brett-zamir.me)
	  // +   bugfixed by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
	  // +   bugfixed by: kirilloid
	  // *     example 1: utf8_decode('Kevin van Zonneveld');
	  // *     returns 1: 'Kevin van Zonneveld'

	  var tmp_arr = [],
	    i = 0,
	    ac = 0,
	    c1 = 0,
	    c2 = 0,
	    c3 = 0,
	    c4 = 0;

	  str_data += '';

	  while (i < str_data.length) {
	    c1 = str_data.charCodeAt(i);
	    if (c1 <= 191) {
	      tmp_arr[ac++] = String.fromCharCode(c1);
	      i++;
	    } else if (c1 <= 223) {
	      c2 = str_data.charCodeAt(i + 1);
	      tmp_arr[ac++] = String.fromCharCode(((c1 & 31) << 6) | (c2 & 63));
	      i += 2;
	    } else if (c1 <= 239) {
	      // http://en.wikipedia.org/wiki/UTF-8#Codepage_layout
	      c2 = str_data.charCodeAt(i + 1);
	      c3 = str_data.charCodeAt(i + 2);
	      tmp_arr[ac++] = String.fromCharCode(((c1 & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
	      i += 3;
	    } else {
	      c2 = str_data.charCodeAt(i + 1);
	      c3 = str_data.charCodeAt(i + 2);
	      c4 = str_data.charCodeAt(i + 3);
	      c1 = ((c1 & 7) << 18) | ((c2 & 63) << 12) | ((c3 & 63) << 6) | (c4 & 63);
	      c1 -= 0x10000;
	      tmp_arr[ac++] = String.fromCharCode(0xD800 | ((c1>>10) & 0x3FF));
	      tmp_arr[ac++] = String.fromCharCode(0xDC00 | (c1 & 0x3FF));
	      i += 4;
	    }
	  }

	  return tmp_arr.join('');
}
