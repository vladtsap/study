package recfun

object Lab1 {

  def main(args: Array[String]): Unit = {
    var pascal_size: Int = 3
    println("-" * 25 + "\n# Task 1 #\nInput: " + pascal_size + "\nOutput:")
    task1(pascal_size)
    println("-" * 25)

    var chars: List[Char] = List('(', ')')
    println("# Task 2 #\nInput: " + chars + "\nOutput:")
    task2(chars)
    println("-" * 25)

    var money: Int = 2
    var coins: List[Int] = List(1, 2)
    println("# Task 3 #\nInput: money = " + money + ", coins = " + coins + "\nOutput:")
    task3(money, coins)
  }

  def task1(size: Int): Unit = {

    def paskal(c: Int, r: Int): Int = {
      if (c == 0 || c == r || r == 0) 1
      else paskal(c - 1, r - 1) + paskal(c, r - 1)
    }

    for (row <- 0 to size) {
      for (col <- 0 to row)
        print(paskal(col, row) + " ")
      println()
    }

  }


  def task2(chars: List[Char]): Unit = {

    def balance(chars: List[Char], left: Int = 0): Boolean = {
      if (chars.isEmpty) true
      else if (chars.head == ')') {
        if (left <= 0) false
        else {
          balance(chars.tail, left - 1)
        }
      }
      else if (chars.head == '(') {
        balance(chars.tail, left + 1)

      }
      else {
        balance(chars.tail, left)
      }
    }

    println(balance(chars))

  }


  def task3(money: Int, coins: List[Int]): Unit = {

    def countChange(money: Int, coins: List[Int], count: Int): Int = {
      if (money < 0) count
      else if (coins.isEmpty)
        if (money == 0) count + 1 else count
      else
        countChange(money - coins.head, coins, count) + countChange(money, coins.tail, count)
    }

    println(countChange(money, coins, 0))

  }


}