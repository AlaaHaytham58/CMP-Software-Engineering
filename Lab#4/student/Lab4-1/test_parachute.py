import unittest
from parachute import ParachuteSytem


class TestParachuteSystem(unittest.TestCase):

    #deploy() 

    def test_deploy_negative_speed(self):
        with self.assertRaises(ValueError):
            ParachuteSytem.deploy(-1, 100)

    def test_deploy_negative_altitude(self):
        with self.assertRaises(ValueError):
            ParachuteSytem.deploy(10, -1)

    def test_deploy_both_negative(self):
        with self.assertRaises(ValueError):
            ParachuteSytem.deploy(-5, -200)

    def test_deploy_successful(self):
        self.assertEqual(ParachuteSytem.deploy(10, 300), "Parachute deployed")

    def test_deploy_too_low_altitude(self):
        self.assertEqual(ParachuteSytem.deploy(30, 100), "Too low to deploy")

    def test_deploy_exact_boundary_altitude(self): # the boundary condition
        self.assertEqual(ParachuteSytem.deploy(10, 150), "Parachute deployed")

    def test_deploy_just_below_boundary_altitude(self):
        self.assertEqual(ParachuteSytem.deploy(10, 149), "Too low to deploy")

    def test_deploy_zero_speed(self):
        self.assertEqual(ParachuteSytem.deploy(0, 300), "Parachute deployed")

    def test_deploy_zero_altitude(self):
        self.assertEqual(ParachuteSytem.deploy(10, 0), "Too low to deploy")

    #---------------------------------------------------------------

    def test_calculate_landing_impact(self):
        self.assertEqual(ParachuteSytem.calculate_landing_impact(50, 100), 500)

    def test_calculate_landing_impact_zero_speed(self):
        self.assertEqual(ParachuteSytem.calculate_landing_impact(0, 100), 0)

    def test_calculate_landing_impact_zero_weight(self):                                        
        self.assertEqual(ParachuteSytem.calculate_landing_impact(50, 0), 0)

    def test_calculate_landing_impact_small_values(self):
        self.assertAlmostEqual(ParachuteSytem.calculate_landing_impact(1, 1), 0.1)

    def test_calculate_landing_impact_large_values(self):
        self.assertEqual(ParachuteSytem.calculate_landing_impact(1000, 500), 50000)

    def test_calculate_landing_impact_negative_speed(self):
        with self.assertRaises(ValueError):
            ParachuteSytem.calculate_landing_impact(-10, 100)

    def test_calculate_landing_impact_negative_weight(self):
        with self.assertRaises(ValueError):
            ParachuteSytem.calculate_landing_impact(10, -100)

    # -----------------------------------------------------------------

    def test_is_safe_landing_safe(self):
        self.assertTrue(ParachuteSytem.is_safe_landing(10, 40))

    def test_is_safe_landing_unsafe(self):
        self.assertFalse(ParachuteSytem.is_safe_landing(50, 100))

    def test_is_safe_landing_at_threshold(self):
        self.assertFalse(ParachuteSytem.is_safe_landing(10, 50))

    def test_is_safe_landing_just_below_threshold(self):
        self.assertTrue(ParachuteSytem.is_safe_landing(1, 49))

    def test_is_safe_landing_zero_speed(self):
        self.assertTrue(ParachuteSytem.is_safe_landing(0, 1000))

    def test_is_safe_landing_negative_speed(self):
        with self.assertRaises(ValueError):
            ParachuteSytem.is_safe_landing(-10, 100)

    def test_is_safe_landing_negative_weight(self):
        with self.assertRaises(ValueError):
            ParachuteSytem.is_safe_landing(10, -100)


if __name__ == '__main__':
    unittest.main()