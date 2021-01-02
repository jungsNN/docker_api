package main

import (
    "log"
    "time"

    "github.com/jungsnn/muxinator"

    "github.com/jungsnn/docker_api/config/controller"
    "github.com/jungsnn/docker_api/config/domain"
    "github.com/jungsnn/docker_api/config/service"

)

func main() {
    config := domain.Config{}

    configService := service.ConfigService{
        Config: &config,
        Location: "config.yaml"
    }

    go configService.Watch(time.Second * 30)

    c := controller.Controller{
        Config: &config,
    }

    router := muxinator.NewRouter()
    router.Get("/read/{serviceName}", c.ReadConfig)
    log.Fatal(router.ListenAndServe(":8080"))
}