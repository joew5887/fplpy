from fplpy.unlinked_object.team.model import TeamModel
from fplpy.unlinked_object.label.model import LabelModel
from fplpy.unlinked_object.position.model import PositionModel
from fplpy.unlinked_object.player.model import PlayerModel
from fplpy.unlinked_object.fixture.model import FixtureModel
from fplpy.unlinked_object.event.model import EventModel
from fplpy.unlinked_object.chip.model import ChipModel


def team_model() -> TeamModel:
    return TeamModel(**
        {
            "code":3,"draw":0,"id":1,"loss":0,"name":"Arsenal",
            "played":0,"points":0,"position":2,"short_name":"ARS","strength":5,
            "unavailable":False,"win":0,"strength_overall_home":1350,
            "strength_overall_away":1350,"strength_attack_home":1390,
            "strength_attack_away":1400,"strength_defence_home":1310,
            "strength_defence_away":1300,"pulse_id":1
        }
    )
    

def label_model() -> LabelModel:
    return LabelModel(label="Goals Scored", name="goals_scored")


def position_model() -> PositionModel:
    return PositionModel(**
        {
            "id":1,"plural_name":"Goalkeepers","plural_name_short":"GKP",
            "singular_name":"Goalkeeper","singular_name_short":"GKP",
            "squad_select":2,"squad_min_select":None,"squad_max_select":None,
            "squad_min_play":1,"squad_max_play":1,"ui_shirt_specific":True,
            "sub_positions_locked":[12],"element_count":82
        }
    )
    
    
def player_model() -> PlayerModel:
    return PlayerModel(**
        {
            "chance_of_playing_next_round":0,
            "chance_of_playing_this_round":0,"code":438098,"cost_change_event":0,
            "cost_change_event_fall":0,"cost_change_start":-1,"cost_change_start_fall":1,
            "dreamteam_count":0,"element_type":3,"ep_next":"0.0","ep_this":"0.0",
            "event_points":0,"first_name":"Fábio","form":"0.0","id":1,"in_dreamteam":False,
            "news":"Has joined Portuguese side FC Porto on loan for the 2024/25 season",
            "news_added":"2024-08-29T11:06:25.241953Z","now_cost":54,"photo":"438098.jpg",
            "points_per_game":"0.0","second_name":"Ferreira Vieira","selected_by_percent":"0.0",
            "special":False,"squad_number":None,"status":"u","team":1,"team_code":3,"total_points":0,"transfers_in":439,
            "transfers_in_event":0,"transfers_out":2825,"transfers_out_event":0,"value_form":"0.0","value_season":"0.0",
            "web_name":"Fábio Vieira","opta_code":"p438098","minutes":0,"goals_scored":0,"assists":0,"clean_sheets":0,"goals_conceded":0,
            "own_goals":0,"penalties_saved":0,"penalties_missed":0,"yellow_cards":0,"red_cards":0,"saves":0,"bonus":0,
            "bps":0,"influence":"0.0","creativity":"0.0","threat":"0.0","ict_index":"0.0",
            "mng_win":0,"mng_draw":0,"mng_loss":0,"mng_underdog_win":0,"mng_underdog_draw":0,"mng_clean_sheets":0,
            "mng_goals_scored":0,"influence_rank":795,"influence_rank_type":343,"creativity_rank":795,
            "creativity_rank_type":343,"threat_rank":791,"threat_rank_type":341,"ict_index_rank":795,
            "ict_index_rank_type":343,"corners_and_indirect_freekicks_order":None,"corners_and_indirect_freekicks_text":""
            ,"direct_freekicks_order":None,"direct_freekicks_text":"","penalties_order":None,"penalties_text":"",
        }
    )
    

def fixture_model() -> FixtureModel:
    return FixtureModel(**
        {
            "code": 2444470,
            "event": 1,
            "finished": True,
            "finished_provisional": True,
            "id": 1,
            "kickoff_time": "2024-08-16T19:00:00Z",
            "minutes": 90,
            "provisional_start_time": False,
            "started": True,
            "team_a": 9,
            "team_a_score": 0,
            "team_h": 14,
            "team_h_score": 1,
            "stats": [
                {
                    "identifier": "goals_scored",
                    "a": [],
                    "h": [
                    {
                        "value": 1,
                        "element": 389
                    }
                    ]
                },
                {
                    "identifier": "assists",
                    "a": [],
                    "h": [
                    {
                        "value": 1,
                        "element": 372
                    }
                    ]
                },
                {
                    "identifier": "own_goals",
                    "a": [],
                    "h": []
                },
                {
                    "identifier": "penalties_saved",
                    "a": [],
                    "h": []
                },
                {
                    "identifier": "penalties_missed",
                    "a": [],
                    "h": []
                },
                {
                    "identifier": "yellow_cards",
                    "a": [
                    {
                        "value": 1,
                        "element": 240
                    },
                    {
                        "value": 1,
                        "element": 241
                    },
                    {
                        "value": 1,
                        "element": 243
                    }
                    ],
                    "h": [
                    {
                        "value": 1,
                        "element": 377
                    },
                    {
                        "value": 1,
                        "element": 382
                    }
                    ]
                },
                {
                    "identifier": "red_cards",
                    "a": [],
                    "h": []
                },
                {
                    "identifier": "saves",
                    "a": [
                    {
                        "value": 4,
                        "element": 248
                    }
                    ],
                    "h": [
                    {
                        "value": 2,
                        "element": 383
                    }
                    ]
                },
                {
                    "identifier": "bonus",
                    "a": [],
                    "h": [
                    {
                        "value": 3,
                        "element": 389
                    },
                    {
                        "value": 2,
                        "element": 594
                    },
                    {
                        "value": 1,
                        "element": 369
                    },
                    {
                        "value": 1,
                        "element": 380
                    }
                    ]
                },
                {
                    "identifier": "bps",
                    "a": [
                    {
                        "value": 16,
                        "element": 249
                    },
                    {
                        "value": 15,
                        "element": 240
                    },
                    {
                        "value": 15,
                        "element": 255
                    },
                    {
                        "value": 13,
                        "element": 245
                    },
                    {
                        "value": 12,
                        "element": 248
                    },
                    {
                        "value": 11,
                        "element": 19
                    },
                    {
                        "value": 10,
                        "element": 251
                    },
                    {
                        "value": 7,
                        "element": 257
                    },
                    {
                        "value": 5,
                        "element": 239
                    },
                    {
                        "value": 5,
                        "element": 241
                    },
                    {
                        "value": 5,
                        "element": 247
                    },
                    {
                        "value": 4,
                        "element": 254
                    },
                    {
                        "value": 4,
                        "element": 259
                    },
                    {
                        "value": 3,
                        "element": 252
                    },
                    {
                        "value": 2,
                        "element": 243
                    },
                    {
                        "value": 2,
                        "element": 256
                    }
                    ],
                    "h": [
                    {
                        "value": 33,
                        "element": 389
                    },
                    {
                        "value": 32,
                        "element": 594
                    },
                    {
                        "value": 26,
                        "element": 369
                    },
                    {
                        "value": 26,
                        "element": 380
                    },
                    {
                        "value": 25,
                        "element": 383
                    },
                    {
                        "value": 22,
                        "element": 377
                    },
                    {
                        "value": 21,
                        "element": 378
                    },
                    {
                        "value": 19,
                        "element": 368
                    },
                    {
                        "value": 11,
                        "element": 364
                    },
                    {
                        "value": 11,
                        "element": 372
                    },
                    {
                        "value": 10,
                        "element": 366
                    },
                    {
                        "value": 5,
                        "element": 385
                    },
                    {
                        "value": 3,
                        "element": 381
                    },
                    {
                        "value": 3,
                        "element": 593
                    },
                    {
                        "value": 2,
                        "element": 371
                    },
                    {
                        "value": -1,
                        "element": 382
                    }
                    ]
                },
                {
                    "identifier": "mng_underdog_win",
                    "a": [],
                    "h": []
                },
                {
                    "identifier": "mng_underdog_draw",
                    "a": [],
                    "h": []
                }
            ],
            "team_h_difficulty": 3,
            "team_a_difficulty": 3,
            "pulse_id": 115827
        },
    )

    
def event_model() -> EventModel:
    return EventModel(**{
      "id": 1,
      "name": "Gameweek 1",
      "deadline_time": "2024-08-16T17:30:00Z",
      "average_entry_score": 57,
      "finished": True,
      "data_checked": True,
      "highest_score": 127,
      "is_previous": False,
      "is_current": False,
      "is_next": False,
      "chip_plays": [
        {
          "chip_name": "bboost",
          "num_played": 144974
        },
        {
          "chip_name": "3xc",
          "num_played": 221430
        }
      ],
      "most_selected": 401,
      "most_transferred_in": 27,
      "top_element": 328,
      "transfers_made": 0,
      "most_captained": 351,
      "most_vice_captained": 351
    })


def chip_model() -> ChipModel:
    return ChipModel(**{
        "id":1,"name":"wildcard","number":1,"start_event":2,"stop_event":19,"chip_type":"transfer"
    })
