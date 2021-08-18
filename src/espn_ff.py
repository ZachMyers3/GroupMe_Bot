from espn_api.football import League


class ESPNLeague:
    def __init__(self, league_id: int = 0, league_year: int = 2021):
        self.league_id = league_id
        self.league_year = league_year

        try:
            self.league = League(self.league_id, self.league_year)
        except Exception as e:
            print(e)
            self.league = None

    def get_scoreboard(self, week: int = None):
        matchups = self.league.scoreboard(week=week)
        if not matchups:
            matchups = self.league.scoreboard(week=1)
        score = [
            (
                f"{match.home_team.team_abbrev} {match.home_score} - "
                f"{match.away_score} {match.away_team.team_abbrev}"
            )
            for match in matchups
            if match.away_team
        ]
        text = [">Score Update"] + score
        return "\n".join(text)

    def get_teams(self):
        teams = [
            (f"{team.owner} - {team.team_name} ({team.team_abbrev})")
            for team in self.league.teams
        ]
        text = [">Teams"] + teams
        return "\n".join(text)

    def get_standings(self):
        wins_dict = {}
        team_dict = {}
        for team in self.league.teams:
            wins_dict[team.team_id] = team.wins
            team_dict[team.team_id] = team

        string_list = []
        wins_dict = dict(sorted(wins_dict.items(), key=lambda item: item[1]))
        print(wins_dict)
        for tid, _ in wins_dict.items():
            team = team_dict[tid]
            string_list.append(
                f"{team.wins}-{team.losses}-{team.ties}\t\t\t{team.team_name}"
            )

        text = [">Standings"] + string_list
        print(text)
        return "\n".join(text)
