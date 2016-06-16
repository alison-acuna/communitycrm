$(".morebutton").click(function(){
  // alert('click')
  $(".morebutton, .editbutton").toggle(display= false);
  $("#more").toggle(display = true);
})

$(".lessbutton").click(function(){
  $("#more").toggle(display = false);
  $(".morebutton, .editbutton").toggle(display = true);
})
