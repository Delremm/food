angular.module('diceApp.directives', []).directive('applyToFirst', [function(){
  return {
    restrict: 'A',
    priority: 10,
    link: function(scope, elm, attrs){
      elm.find(':first').addClass(attrs.applyToFirst);
      console.log(attrs.selector);
      console.log(attrs.applyToFirst);
    }
  }
}]);
/*.directive('description', ['$http', '$templateCache', function ($http, $templateCache){
  return {
    restrict: 'A',
    link: function(scope, elm, attrs){
      function load_description(){
        var desc_url = '/configuration/'+attrs.descSlug+'/';
        $('#'+attrs.descDestinationId).html('Загрузка...');
        $http.get(desc_url, { cache: $templateCache }).success(function(data) {
            $('#'+attrs.descDestinationId).html(data);
            $('#'+attrs.descDestinationId).append($(elm).find("div.description").html());
        });
      }
      elm.bind('mouseenter', load_description);
      // $(elm).parent().hover(
      //   function(){
      //     scope.load_description();
      //     //$('#'+attrs.descDestinationId).html(elm.html());
      //   },
      //   function(){
      //     //$('#'+attrs.descDestinationId).text('');
      //   }
      // );
      
    }
  }
}]);
*/