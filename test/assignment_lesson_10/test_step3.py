import io
import sys
from unittest import mock

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator


class TestStep3(AssignmentTester):
    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_1_name(self, mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_name_valid('Alon')
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_1_name_2(self, mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_name_valid('A')
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_1_name_3(self, mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_name_valid('')
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_2_board_size_1(self, mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_board_size_valid(0)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_2_board_size_2(self, mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_board_size_valid(-1)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_2_board_size_3(self, mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_board_size_valid(7)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_3_number_of_mines_1(self,mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_number_of_mines_valid(5, 0)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_3_number_of_mines_2(self, mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_number_of_mines_valid(5, 13)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_3_number_of_mines_3(self, mock_input, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_number_of_mines_valid(5, 7)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['D', '9', '40'])
    def test_full_interaction_wrong_name_verify_return(self, mock_input, mock_stdout, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        real_result = user_interaction.register_user()
        # verify
        expected_result = (None, None, None)
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['D', '9', '40'])
    def test_full_interaction_wrong_name_verify_output(self, mock_input, mock_stdout, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        user_interaction.register_user()
        # verify
        expected_result = "Your name is too short\n"
        real_result = mock_stdout.getvalue()
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '0', '40'])
    def test_full_interaction_wrong_board_size_verify_return(self, mock_input, mock_stdout, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        real_result = user_interaction.register_user()
        # verify
        expected_result = (None, None, None)
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '0', '40'])
    def test_full_interaction_wrong_board_size_verify_output(self, mock_input, mock_stdout, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        user_interaction.register_user()
        # verify
        expected_result = "Dan, you entered illegal board size\n"
        real_result = mock_stdout.getvalue()
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '9', '2'])
    def test_full_interaction_wrong_mines_verify_return(self, mock_input, mock_stdout, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        real_result = user_interaction.register_user()
        # verify
        expected_result = (None, None, None)
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '9', '2'])
    def test_full_interaction_wrong_mines_verify_output(self, mock_input, mock_stdout, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction
        user_interaction.register_user()
        # verify
        expected_result = "Dan, you entered illegal number of mines\n"
        real_result = mock_stdout.getvalue()
        self.assertEqualWithMessage(real_result, expected_result, msg=message)


    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_full_interaction(self, mock_input, mock_stdout, message):
        # test
        ######
        import project.ui.user_interaction as user_interaction

        expected_result = ('Dan', 9, 40)
        real_result = user_interaction.register_user()
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)