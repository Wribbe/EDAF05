import java.util.*;
import java.nio.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.Charset;
import java.io.*;

class Runme {

    // needed data structures
    private static Integer[] current_partners;
    private static List<List<Integer>> preferences;
    private static String[] names;

    public static void main(String[] args) {

        // pad structures so index 0 is not used
        String filename = args[0];
        List<String> lines = new ArrayList<String>();
        int n = 0;

        // read lines from file and parse them
        try {
            lines = Files.readAllLines(Paths.get(filename), Charset.defaultCharset());
        } catch (IOException e) {
            e.printStackTrace();
        }
        List<String> parsedLines = new ArrayList<String>();
        for (String line : lines) {
            if (line.startsWith("#")) {
                continue;
            } else if (line.startsWith("n")) {
                n = Integer.valueOf(line.split("=")[1]);
                continue;
            }
            parsedLines.add(line);
        }

        // initialize data structures
        current_partners = new Integer[n*2+1];
        preferences = new ArrayList<List<Integer>>(n*2+1);
        preferences.add(new ArrayList<Integer>());
        names = new String[n*2+1];

        names[0] = "-1";
        current_partners[0] = -1;

        // parse the input and store it in name- or preference-structure
        boolean doing_preferences = false;
        for (String line : parsedLines) {
            if (line.equals("")) {
                doing_preferences = true;
                continue;
            }
            if (!doing_preferences) {
                // put in names
                String[] tokens = line.split(" ");
                int id = Integer.valueOf(tokens[0]);
                String name = tokens[1];
                names[id] = name;
                current_partners[id] = -1;
                preferences.add(new ArrayList<Integer>());
            } else {
                // put in preferences
                String[] tokens = line.split(":");
                int id = Integer.valueOf(tokens[0]);
                String[] preference_tokens = tokens[1].split(" ");
                List<Integer> current_preferences = new ArrayList<Integer>();
                for (String preference : preference_tokens) {
                    if (preference.equals("")) {
                        continue;
                    }
                    int id_value = Integer.valueOf(preference.trim());
                    current_preferences.add(id_value, id_value);
                }
                preferences.add(id, current_preferences);
            }
        }

        // initialize the male_stack
        Stack<Integer> male_stack = new Stack<Integer>();
        for(int i=1; i<n*2+1; i = i+2) {
            male_stack.push(i);
        }
        
        // iterate through the male_stack until empty
        int current_male;
        while(!male_stack.isEmpty()) {
            current_male = male_stack.pop();
            List<Integer> male_preferences = preferences.get(current_male);
            for (Integer female_id : male_preferences) {
                int match_return = match(current_male, female_id);
                if (match_return == 0) {
                    // she prefers the current to the new one
                    continue;
                } else if (match_return > 0) { // she prefers the new one to the current returns current male_stack.push(match_return);
                    break;
                } else if (match_return < 0) {
                    // there was an instantaneous match
                    break;
                }
            }
        }
        int male_name_index, female_name_index;
        for(int i = 1; i<n*2+1; i = i+2) {
            male_name_index = i;
            female_name_index = current_partners[male_name_index];
            System.out.println(String.format("%s -- %s",
                        names[male_name_index],
                        names[female_name_index]));
        }
    }
    public static int match(int male_id, int female_id) {
        int current_index, new_index;
        int current_male = current_partners[female_id];
        if (current_male < 0) {
            current_partners[female_id] = male_id;
            current_partners[male_id] = female_id;
            return -1;
        }
        List<Integer> female_preference = preferences.get(female_id);
        for (Integer pref_id : female_preference) {
            i
            new_index = female_preference.indexOf(male_id);
            current_index = female_preference.indexOf(current_male);
            if (current_index < new_index) {
                return 0;
            } else if (new_index < current_index) {
                current_partners[female_id] = male_id;
                current_partners[male_id] = female_id;
                current_partners[current_male] = -1;
                return current_male;
            }
        }
        return -4;
    }
}
