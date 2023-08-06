"""Tests for the Match class."""
# pyright: reportMissingSuperCall=false
from unittest import IsolatedAsyncioTestCase, TestCase, main
from pathlib import Path

from algobattle.cli import parse_cli_args
from algobattle.battle import Fight, Iterated, Averaged
from algobattle.match import BaseConfig, Match, MatchConfig
from algobattle.team import Team, Matchup, TeamHandler, TeamInfo
from algobattle.docker_util import ProgramConfig, ProgramRunInfo, RunParameters
from .testsproblem.problem import TestProblem


class TestTeam(Team):
    """Team that doesn't rely on actual docker images."""

    def __init__(self, team_name: str) -> None:
        self.name = team_name


def dummy_result(*score: float) -> list[Fight]:
    """Creates a list of dummy results for testing."""
    return [
        Fight(
            score=s,
            max_size=0,
            generator=ProgramRunInfo(
                params=RunParameters(),
                runtime=0,
            ),
            solver=ProgramRunInfo(
                params=RunParameters(),
                runtime=0,
            ),
        )
        for s in score
    ]


class Matchtests(TestCase):
    """Tests for the match object."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up a match object."""
        cls.team0 = TestTeam("0")
        cls.team1 = TestTeam("1")
        cls.matchup0 = Matchup(cls.team0, cls.team1)
        cls.matchup1 = Matchup(cls.team1, cls.team0)
        cls.team_dict = {
            "active_teams": [cls.team0.name, cls.team1.name],
            "excluded_teams": [],
        }
        cls.teams = TeamHandler([cls.team0, cls.team1])

    def test_all_battle_pairs_two_teams(self):
        """Two teams both generate and solve one time each."""
        self.assertEqual(self.teams.matchups, [self.matchup0, self.matchup1])

    def test_all_battle_pairs_single_player(self):
        """A team playing against itself is the only battle pair in single player."""
        teams = TeamHandler([self.team0])
        self.assertEqual(teams.matchups, [Matchup(self.team0, self.team0)])

    def test_calculate_points_zero_rounds(self):
        """All teams get 0 points if no rounds have been fought."""
        match = Match(**self.team_dict)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 0, self.team1.name: 0})

    def test_calculate_points_iterated_no_successful_round(self):
        """Two teams should get an equal amount of points if nobody solved anything."""
        match = Match(**self.team_dict)
        battle = Iterated()
        battle.results = [0]
        match.insert_battle(battle, self.matchup0)
        match.insert_battle(battle, self.matchup1)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 50, self.team1.name: 50})

    def test_calculate_points_iterated_draw(self):
        """Two teams should get an equal amount of points if both solved a problem equally well."""
        match = Match(**self.team_dict)
        battle = Iterated()
        battle.results = [20]
        match.insert_battle(battle, self.matchup0)
        match.insert_battle(battle, self.matchup1)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 50, self.team1.name: 50})

    def test_calculate_points_iterated_domination(self):
        """One team should get all points if it solved anything and the other team nothing."""
        match = Match(**self.team_dict)
        battle = Iterated()
        battle.results = [10]
        battle2 = Iterated()
        battle2.results = [0]
        match.insert_battle(battle, self.matchup0)
        match.insert_battle(battle2, self.matchup1)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 0, self.team1.name: 100})

    def test_calculate_points_iterated_one_team_better(self):
        """One team should get more points than the other if it performed better."""
        match = Match(**self.team_dict)
        battle = Iterated()
        battle.results = [10]
        battle2 = Iterated()
        battle2.results = [20]
        match.insert_battle(battle, self.matchup0)
        match.insert_battle(battle2, self.matchup1)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 66.7, self.team1.name: 33.3})

    def test_calculate_points_averaged_no_successful_round(self):
        """Two teams should get an equal amount of points if nobody solved anything."""
        match = Match(**self.team_dict)
        battle = Averaged()
        battle.fight_results = dummy_result(0, 0, 0)
        match.insert_battle(battle, self.matchup0)
        match.insert_battle(battle, self.matchup1)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 50, self.team1.name: 50})

    def test_calculate_points_averaged_draw(self):
        """Two teams should get an equal amount of points if both solved a problem equally well."""
        match = Match(**self.team_dict)
        battle = Averaged()
        battle.fight_results = dummy_result(0.5, 0.5, 0.5)
        match.insert_battle(battle, self.matchup0)
        match.insert_battle(battle, self.matchup1)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 50, self.team1.name: 50})

    def test_calculate_points_averaged_domination(self):
        """One team should get all points if it solved anything and the other team nothing."""
        match = Match(**self.team_dict)
        battle = Averaged()
        battle.fight_results = dummy_result(0, 0, 0)
        battle2 = Averaged()
        battle2.fight_results = dummy_result(1, 1, 1)
        match.insert_battle(battle, self.matchup0)
        match.insert_battle(battle2, self.matchup1)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 100, self.team1.name: 0})

    def test_calculate_points_averaged_one_team_better(self):
        """One team should get more points than the other if it performed better."""
        match = Match(**self.team_dict)
        battle = Averaged()
        battle.fight_results = dummy_result(0.6, 0.6, 0.6)
        battle2 = Averaged()
        battle2.fight_results = dummy_result(0.4, 0.4, 0.4)
        match.insert_battle(battle, self.matchup0)
        match.insert_battle(battle2, self.matchup1)
        self.assertEqual(match.calculate_points(100), {self.team0.name: 40, self.team1.name: 60})

    # TODO: Add tests for remaining functions


class Execution(IsolatedAsyncioTestCase):
    """Some basic tests for the execution of the battles."""

    @classmethod
    def setUpClass(cls) -> None:
        problem_path = Path(__file__).parent / "testsproblem"
        cls.problem = TestProblem
        run_params = RunParameters(timeout=2)
        cls.config = BaseConfig(
            program=ProgramConfig(generator=run_params, solver=run_params),
            battle={
                "Iterated": Iterated.BattleConfig(maximum_size=10, rounds=2),
                "Averaged": Averaged.BattleConfig(instance_size=5, num_fights=3),
            },
        )
        cls.generator = problem_path / "generator"
        cls.solver = problem_path / "solver"

    async def test_basic(self):
        self.config.teams = {"team_0": TeamInfo(generator=self.generator, solver=self.solver)}
        self.config.match.battle_type = "Iterated"
        await Match.run(self.config, TestProblem)

    async def test_multi_team(self):
        team0 = TeamInfo(generator=self.generator, solver=self.solver)
        team1 = TeamInfo(generator=self.generator, solver=self.solver)
        self.config.teams = {"team_0": team0, "team_1": team1}
        self.config.match.battle_type = "Iterated"
        await Match.run(self.config, TestProblem)

    async def test_averaged(self):
        self.config.teams = {"team_0": TeamInfo(generator=self.generator, solver=self.solver)}
        self.config.match.battle_type = "Averaged"
        await Match.run(self.config, TestProblem)


class Parsing(TestCase):
    """Testing the parsing of CLI and config files."""

    @classmethod
    def setUpClass(cls) -> None:
        path = Path(__file__).parent
        cls.problem_path = path / "testsproblem"
        cls.configs_path = path / "configs"
        cls.teams = {"team_0": TeamInfo(generator=cls.problem_path / "generator", solver=cls.problem_path / "solver")}

    def test_no_cfg_default(self):
        _, cfg = parse_cli_args([str(self.problem_path)])
        self.assertEqual(cfg, BaseConfig(teams=self.teams))

    def test_empty_cfg(self):
        _, cfg = parse_cli_args([str(self.problem_path), "--config", str(self.configs_path / "empty.toml")])
        self.assertEqual(cfg, BaseConfig(teams=self.teams))

    def test_cfg(self):
        _, cfg = parse_cli_args([str(self.problem_path), "--config", str(self.configs_path / "test.toml")])
        self.assertEqual(
            cfg,
            BaseConfig(
                teams=self.teams,
                match=MatchConfig(
                    points=10,
                    battle_type="Averaged",
                ),
                program=ProgramConfig(generator=RunParameters(space=10)),
                battle={
                    "Averaged": Averaged.BattleConfig(num_fights=1),
                },
            ),
        )

    def test_cli(self):
        exec_config, _ = parse_cli_args([str(self.problem_path), "-s"])
        self.assertTrue(exec_config.silent)

    def test_cli_no_problem_path(self):
        with self.assertRaises(SystemExit):
            parse_cli_args([])

    def test_cfg_team(self):
        _, cfg = parse_cli_args([str(self.problem_path), f"--config={self.configs_path / 'teams.toml'}"])
        self.assertEqual(
            cfg,
            BaseConfig(
                teams={
                    "team 1": TeamInfo(generator=Path(), solver=Path()),
                    "team 2": TeamInfo(generator=Path(), solver=Path()),
                }
            ),
        )

    def test_cfg_team_no_name(self):
        with self.assertRaises(ValueError):
            parse_cli_args([str(self.problem_path), f"--config={self.configs_path / 'teams_incorrect.toml'}"])


if __name__ == "__main__":
    main()
