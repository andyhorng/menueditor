angular.module("menuEditorApp", ['ui.bootstrap', 'ui.router'])
    .config ($stateProvider) ->
        $stateProvider
            .state 'list', {
                url: "/",
                templateUrl: "/assets/templates/list.html"
            }
            .state 'menu', {
                url: "/:id"
                templateUrl: "/assets/templates/menu.html"
            }

    .controller "MenuListController", ($http, $modal, $rootScope, $window) ->

        @menus = []

        $http.get('/api/menu')
            .success (data) =>
                @menus = data

        @newMenu = () =>
            modalInstance = $modal.open
                templateUrl: "/assets/templates/new.html"
                controller: ($scope, $modalInstance, $http) ->

                    $scope.menu = {}

                    $scope.save = () =>
                        $http
                            .post("/api/menu", $scope.menu)
                            .success (data) ->
                                $modalInstance.close(data)

                    $scope.cancel = () =>
                        $modalInstance.dismiss("cancel")

                    return @


            modalInstance.result.then (rt) =>
                @menus.push rt

        @deleteMenu = (ix, menuId) =>
            if $window.confirm("Are you sure?")
                $http
                    .delete("/api/menu/#{menuId}")
                    .success =>
                        @menus.splice(ix, 1)
                        $rootScope.$emit "alert",
                            type: "success"
                            msg: "Deleted"



        # coffee will return last statement, so return the right one manually
        return @

    .controller "MenuController", ($http, $stateParams, $rootScope) ->

        @menu = {}

        $http
            .get("/api/menu/#{$stateParams.id}")
            .success (data) =>
                @menu = data

        @save = (menu) =>
            # unset menu.id
            delete menu.id

            $http
                .patch("/api/menu/#{$stateParams.id}", menu)
                .success (data) =>
                    $rootScope.$emit "alert",
                        type: "success"
                        msg: "Success"

        @addAddress = () =>
            @menu.addresses ||= []
            @menu.addresses.push({})

        @removeAddress = (ix) =>
            @menu.addresses.splice(ix, 1)

        @addBusinessHour = () =>
            @menu.business_hours ||= []
            @menu.business_hours.push({})

        @removeBusinessHour = (ix) =>
            @menu.business_hours.splice(ix, 1)

        @addItem = () =>
            @menu.items ||= []
            @menu.items.push({customs: angular.copy(@customs)})

        @removeItem = (ix) =>
            @menu.items.splice(ix, 1)

        @customs =
            hotcold: ['冷', '熱']
            ice: ['正常', '少冰', '微冰', '去冰']
            sweet: ['正常', '少糖', '半糖', '微糖', '無糖']
            size: ['小', '中', '大', '特大', '巨無霸']


        return @
    .controller "AlertController", ($rootScope, $timeout) ->
        @alerts = []

        @closeAlert = () =>
            @alerts.shift()

        $rootScope.$on "alert", (e, alert) =>
            @alerts.push alert
            $timeout @closeAlert, 3000

        return @
