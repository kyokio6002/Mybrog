$(function(){
  var r = {};
function D(v) { this['version'] = v; }
try { r["jQuery"] = new D(jQuery.fn.jquery); } catch(e) {}
try { r["jQuery UI"] = new D(jQuery.ui.version); } catch(e) {}
try { r["Vue"] = new D(Vue.version); } catch(e) {}
try { r["React"] = JSON.stringify(window.__REACT_DEVTOOLS_GLOBAL_HOOK__._renderers).match(/"version"\:"([\d\.]+)"/)[1]; } catch(e) {}
try { r["Angular"] = new D($('[ng-version]').getAttribute('ng-version')) } catch(e) {}
try { r["AngularJS"] = new D(angular.version.full) } catch(e) {}
try { r["Babel"] = new D(Babel.version) } catch(e) {}
try { r["lodash"] = new D(_.VERSION) } catch(e) {}
try { r["Moment.js"] = new D(moment.version) } catch(e) {}
try { r["Backbone.js"] = new D(Backbone.VERSION) } catch(e) {}
try { r["Riot.js"] = new D(riot.version) } catch(e) {}
try { r["Knockout.js"] = new D(ko.version) } catch(e) {}
try { r["D3.js"] = new D(d3.version) } catch(e) {}
try { r["Polymer"] = new D(Polymer.version) } catch(e) {}
console.table(r);
	var
	  winW = $(window).width(),
		winH = $(window).height(),
		nav = $('#mainnav ul a'),
		curPos = $(this).scrollTop();
	
	if (winW < 880){
		var headerH =0;
	}
	else{
		var headerH =63;
	}
	
	$(nav).on('click', function(){
		nav.removeClass('active');
  	var $el = $(this),
		id = $el.attr('href');
 		$('html, body').animate({
   		scrollTop: $(id).offset().top - headerH
 		}, 500);
		$(this).addClass('active');
		if (winW < 880){
			$('#menuWrap').next().slideToggle();
			$('#menuBtn').removeClass('close');
		}
 		return false;
	});
	
	var timer = false;
	$(window).bind('load resize',function(){	
		if (timer !== false){clearTimeout(timer);}
		timer = setTimeout(function(){
			var
				w = $(window).innerWidth(),
				bg = $('.bg'),
				bgH = bg.height();
			
			if(w > 800){
				$(function(){		
			  	$(".vMid").css('height', bgH);
				});
			}
			else{
				$(function(){		
			  	$(".vMid").css({'height':'auto','padding':'50px 20px'});
				});
			}		
		});
	});
	
	$('.panel').hide();
	$('#menuWrap').toggle(function(){
		$(this).next().slideToggle();
		$('#menuBtn').toggleClass('close');
	},
	function(){
		$(this).next().slideToggle();
		$('#menuBtn').removeClass('close');
	});
		
	$(window).on('scroll', function(){
		var curPos = $(this).scrollTop();
		if(curPos > 80){
			$('#mainnav').addClass('changeNav');
		}
		else{
			$('#mainnav').removeClass('changeNav');
		}
	});


});
