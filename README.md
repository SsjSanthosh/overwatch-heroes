## Overwatch Heroes - a Django API for hero stats!

![Project thumbnail](https://raw.githubusercontent.com/SsjSanthosh/overwatch-heroes/master/screenshots/thumbnail.png)

A django REST API built with DRF, gathering stats and information on all the 32 heroes in the Overwatch game. Get the react/frontend repo [here](https://github.com/SsjSanthosh/overwatch-heroes-react)

## Table of Contents

- [Project Status](#project-status)
- [Description](#description)
- [Motivation](#motivation)
- [Tech/Framework Used](#techframework-used)
- [Endpoints](#endpoints)
- [Examples](#example)
- [Installation](#installation)
- [Possible Future Updates](#possible-future-updates)

## Project Status

I want to take this app forward and include more information about the game, perhaps even add competitive stats.

## Description

A Rest API built from the ground up to be the best resource for getting stats and information about the heroes in the game overwatch. Exhaustive list of information regarding the heroes, sourced from the wiki and the official Playoverwatch website.

## Tech/Framework Used

- Django
- Django Rest Framework
- Python

## Endpoints

- /heroes - Gets all the heroes, just their name, preview_image, and role.
- heroes/details/{id} - Get the hero details for the particular hero id.

## Filters

- role - filter by role, one of `[Tank, Damage, Support]`
  Example - [https://overwatch-heroes-api.herokuapp.com/api/v1/heroes/details/?role=Tank](https://overwatch-heroes-api.herokuapp.com/api/v1/heroes/details/?role=Tank)
- name - filter by name
  Example - [https://overwatch-heroes-api.herokuapp.com/api/v1/heroes/details/?name=Reinhardt](https://overwatch-heroes-api.herokuapp.com/api/v1/heroes/details/?name=Reinhardt)

More filters coming soon!

## Motivation

I built this to be able to get all the information about these characters in one place. I realized there was no current API with the latest stats, so I went ahead and built one! Of course, I also built a react client to showcase the data in a meaningful way. Using Django and DRF to build the backend API was an experience for sure, I hit quite a bit of stumbling blocks and had to do a lot of googling but in the end, it came together quite nicely. I am hoping to make this an overwatch one-stop-shop for players, especially the API, with more info about maps, plot, comics and more!

## Examples

##### Example Preview hero route -

[https://overwatch-heroes-api.herokuapp.com/api/v1/heroes/](https://overwatch-heroes-api.herokuapp.com/api/v1/heroes/)

`{ id: 2, name: "Ashe", role: "Damage", preview_image: "static/img/ashe-preview.png" }, { id: 6, name: "Baptiste", role: "Support", preview_image: "static/img/baptiste-preview.png" }, { id: 14, name: "Bastion", role: "Damage", preview_image: "static/img/bastion-preview.png" }, { id: 32, name: "Brigitte", role: "Support", preview_image: "static/img/brigitte-preview.png" }`

##### Example of a hero -

[https://overwatch-heroes-api.herokuapp.com/api/v1/heroes/details/2/](https://overwatch-heroes-api.herokuapp.com/api/v1/heroes/details/2/)

`{name: "Ashe", id: 2, image: "static/img/ashe.png", wiki_link: "https://overwatch.gamepedia.com/Ashe", favourite_quote: "My business, My rules.", sound: "static/audio/ashe.oga", real_name: "Elizabeth Caledonia "Calamity" Ashe", affiliation: "Deadlock Gang", age: 39, difficulty: 2, health: "200", shield: null, armour: null, role: "Damage", occupation: "Thief, Gang Leader", weapon: [ { name: "The Viper", image: "static/img/ashe-weapon.png", aim_type: "Histcan", damage: "20-40 (Hip Fire),40-80(ADS)", movement_speed: "-25% penalty", rate_of_fire: "4 shots per second (Hip fire),~1.42 shots per second (ADS)", ammo: "12", headshot: "True", spread: "Max:1.85 degrees(Hip fire),Pinpoint(ADS)", falloff_range: "30 to 50 meters" } ], ultimate: { name: "Bob", image: "static/img/ashe-ultimate.png", aim_type: "Hitscan (arm cannon)", cost: "2240", casting_time: "", movement_speed: "15 meters per second", duration: 10, damage: "Charge:120, Arm cannon: 112 per second, 14 per bullet, 1092 overall", healing: "", description: "Ashe summons her trusted omnic sidekick, B.O.B., who charges forward and knocks enemies into the air, then lays down suppressing fire with his arm cannons." }, abilities: [ { name: "Dynamite", image: "static/img/ashe-dynamite.png", cooldown: "12 seconds", damage: "Explosion:30-75, Burn:100, Self:50%", description: "Ashe throws an explosive that detonates after a short delay or immediately when shot. The explosion from Dynamite also lights enemies on fire, dealing damage over time.", type: "Arcing projectile", healing: "", casting_time: "2 seconds delay", movement_speed: "" }, { name: "Coach Gun", image: "static/img/ashe-coach.png", cooldown: "10 seconds", damage: "6 per pellet, 15 total pellets, 90 per shot", description: "Ashe blasts enemies in front of her, knocking them away and propelling herself backward for added mobility.", type: "shotgun (hitscan)", healing: "", casting_time: "", movement_speed: "" } ], preview_image: "static/img/ashe-preview.png" }`

## Installation

Clone down this repository.

Installation:

- Create a virtual environment
- Pip install everything in the requirements.txt

To Start Server:

`python manage.py runserver`

To Visit App:

`localhost:8000/`

## Possible Future Updates

- Add more filters, better routes
- Add more information regarding the game
