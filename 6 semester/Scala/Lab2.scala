object Lab2 {

  def main(args: Array[String]): Unit = {
    println(contains(singletonSet(1), 1))
  }

  type Set = Int => Boolean

  def contains(s: Set, elem: Int): Boolean = s(elem)

  def singletonSet(elem: Int): Set = (x: Int) => x == elem

  def union(s: Set, t: Set): Set = (x: Int) => s(x) || t(x)

  def intersect(s: Set, t: Set): Set = (x: Int) => s(x) && t(x)

  def diff(s: Set, t: Set): Set = (x: Int) => s(x) && !t(x)

  def filter(s: Set, p: Int => Boolean): Set = (x: Int) => s(x) && p(x)

  val bound = 1000

  def forall(s: Set, p: Int => Boolean): Boolean = {
    def iter(a: Int): Boolean = {
      if (a > bound) true
      else if (s(a) && !p(a)) false
      else iter(a + 1)
    }

    iter(-bound)
  }

  def exists(s: Set, p: Int => Boolean): Boolean = !forall(s, x => !p(x))

  def map(s: Set, f: Int => Int): Set = (y: Int) => exists(s, x => f(x) == y)

}
