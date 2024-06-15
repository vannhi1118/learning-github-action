import add from '../utils/utils'

describe('testing add function', () => {
    test('empty string should result in zero', () => {
      expect(add(1, 2)).toBe(3);
    });
  });