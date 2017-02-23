import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Etl {
  public Map<String, Integer> transform(Map<Integer, List<String>> old) {
    Map<String, Integer> newData = new HashMap<String, Integer>();
    for (Integer score : old.keySet()) {
      for (String letter : old.get(score)) {
        newData.put(letter.toLowerCase(), score);
      }
    }
    return newData;
  }
}
