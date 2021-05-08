/*
This functions are a support to avoid undesired behaviours on creation or
modification of course's overview
*/
$(document).ready(function(){
  $('#id_overview').on("keyup",function(){
    const old_text = $('#id_overview').val();
    const new_text = old_text.replaceAll('`', '');
    document.getElementById("id_overview").value=new_text;
  });
});
$(document).ready(function(){
  $('#new_overview').on("keyup",function(){
    const old_text = $('#new_overview').val();
    const new_text = old_text.replaceAll('`', '');
    document.getElementById("new_overview").value=new_text;
  });
});
