import add from '../utils/utils'

describe('testing add function', () => {
    test('1 + 2 should equal 3', () => {
      expect(add(1, 2)).toBe(3);
    });
  });