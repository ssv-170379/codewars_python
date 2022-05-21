"""
Stacked Balls - 3D (triangle base)
https://www.codewars.com/kata/5bbad1082ce5333f8b000006
"""
"""
Background

I have stacked some cannon balls in a triangle-based pyramid.

Like this,
https://i.imgur.com/ut4ejG1.png [cannon balls triangle base]
Kata Task

Given the number of layers of my stack, what is the total height?

Return the height as multiple of the ball diameter.
Example

The image above shows a stack of 3 layers.
Notes

    layers >= 0
    approximate answers (within 0.001) are good enough

"""


def stack_height_3d(layers):
    if not layers:
        return 0
    else:
        return 1 + ((2 / 3) ** 0.5) * (layers - 1)  # https://mathforums.com/threads/height-of-stack-of-spheres-in-pyramid-fashion.19971/post-82714
        # 1 - bottom layer is = diameter (full height). sqrt(2/3) * layers-1 - all upper layers are of this height


if __name__ == '__main__':
    import codewars_test as test


    @test.describe('Example Tests')
    def example_tests():
        @test.it('Example Test Cases')
        def example_test_cases():
            test.assert_equals(stack_height_3d(1), 1)
            test.assert_approx_equals(stack_height_3d(2), 1.816, margin=0.001, message=None)
