$('#subscribe_email_btn').click(function() {
    var subscriber_email = $("#subscriber_email").val();
    // Send the data using post
    $.get( "{% url 'emailer:subscribe' %}", {email: subscriber_email}, function( data ) {
      if (data.success){
        $( "#subscribe_block" ).empty().append(data.message);
      } else {
        $( "#subcriber_error" ).empty().append(data.message);
      };
    }, "json");
});