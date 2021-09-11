// Courses/update.html
$(document).ready(function(){
  $('input[name="new_overview"],textarea').on("keyup",function(){
    // Here we substitute all backticks symbols ( ` ) for empty spaces ''
    const old_text = $('#new_overview').val();
    const new_text = old_text.replaceAll('`', '');
    document.getElementById("new_overview").value=new_text;
  });
});




// *********************************************************************


// SignUpIn/signupin.html
var idies;
var content;
function tippies(idies,content){
  tippy(idies, {
    content: content,
    placement: 'right-start',
    interactive: true,
  });
}
tippies('#help-username_r','Your username must be unique and its maximum\
                          length is of 150 alphanumerical characters');
tippies('#help-firstname','Your first name(s) can have as maximum of\
                          150 alphanumerical characters of length');
tippies('#help-lastname','Your last name(s) can have as maximum of\
                          150 alphanumerical characters of length');
tippies('#help-email','This field is not mandatory but it can help to\
                     others users and administrators to get in touch with\
                     you');
tippies('#help-password1','Is recommended that your password have 10 or \
                         more alphanumerical characters');

