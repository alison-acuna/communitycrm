$(".morebutton").click(function(){
  // alert('click')
  $(this).toggle(display= false);
  $("#more").toggle(display = true);
})

$(".lessbutton").click(function(){
  $("#more").toggle(display = false);
  $(".morebutton").toggle(display = true);
})
