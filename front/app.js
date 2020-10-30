		'use strict';

		var interfaceApp = angular.module('interfaceApp', [
		    'ui.bootstrap'
		]);


		interfaceApp.controller('intervCtrl', 
			function($scope, $http){
				$http.get("http://127.0.0.1:8000")
		  		.then(function successCallBack(response){
		        	$scope.interventions = response.data;
		    	})
		 		console.log($scope);
			}
		);	
		interfaceApp.controller("modalAccountFormController", ['$scope', '$modal', '$log', 
		    function ($scope, $modal, $log) {

		        $scope.showForm = function () {
		        	$scope.libelle = null;
		    		$scope.description = null;
		    		$scope.nom_inter = null;
		    		$scope.lieu = null;
		    		$scope.date_inter = null;

		            $scope.message = "Show Form Button Clicked";
		            console.log($scope.message);

		            var modalInstance = $modal.open({
		                templateUrl: 'modal-form.html',
		                controller: ModalInstanceCtrl,
		                scope: $scope,
		            });

		            modalInstance.result.then(function (selectedItem) {
		                $scope.selected = selectedItem;
		            });
		        };

		        $scope.modifyForm = function (id,libelle,description,nom_inter,lieu,date_inter) {
				    $scope.id = id;
				    $scope.libelle = libelle;
				    $scope.description = description;
				    $scope.nom_inter = nom_inter;
				    $scope.lieu = lieu;
				    $scope.date_inter = date_inter;



		            var modalInstance = $modal.open({
		                templateUrl: 'modify-inter.html',
		                controller: ModalInstanceCtrl,
		                scope: $scope,
		            });
		            modalInstance.result.then(function (selectedItem) {
		                $scope.selected = selectedItem;
		            });
		        };
            }]);

		var ModalInstanceCtrl = function ($scope, $http, $modalInstance) {

		// Request to get the data from the api
		    $scope.postInterv = function (libelle,description,nom_inter,lieu,date_inter) {
		    	var data = {
		    		libelle		: libelle,
		    		description	: description,
		    		nom_inter 	: nom_inter,
		    		lieu 		: lieu,
		    		date_inter	: date_inter,
		    		statut	    : "B", 

		    	}
		    	$http.post("http://127.0.0.1:8000", JSON.stringify(data))
		    		.then(function(response)
		    		{
		    			console.log(response);
		    		})
 				location.reload(); //Refresh the page to show the last intervention
		    };

		    //function to cancel the new intervention
		    $scope.cancel = function () {
		        $modalInstance.dismiss('cancel');
		    };

		    //function to delete an intervention 
		    //Take the parameter of the intervention and do a delete request to the api and close the modal
		    $scope.delete = function (id) {
		    	$http.delete("http://127.0.0.1:8000/" +id+ "/")
		    	$modalInstance.dismiss('cancel');
 		    };

 		    //function to modify an intervention
 		    $scope.putInterv = function (id,libelle,description,nom_inter,lieu,date_inter) {
		    	var data = {
		    		libelle		: libelle,
		    		description	: description,
		    		nom_inter 	: nom_inter,
		    		lieu 		: lieu,
		    		date_inter	: date_inter,
		    		statut	    : "B", 

		    	}
		    	$http.put("http://127.0.0.1:8000/" +id + "/", JSON.stringify(data))
		    		.then(function(response)
		    		{
		    			console.log(response);
		    		})
		     	location.reload(); 

		    };
		};
