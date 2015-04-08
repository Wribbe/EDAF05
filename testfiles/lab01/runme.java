import java.util.*;
import java.nio.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.Charset;
import java.io.*;

class Runme {
    public static void main(String[] args) {
        String filename = args[0];
        List<String> lines = new ArrayList<String>();
        int n = 0;
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

        Integer[] current_partners = new Integer[n*2+1];
        current_partners[0] = -1;

        List<List<Integer>> preferences = new ArrayList<List<Integer>>(n*2+1);

        String[] names = new String[n*2+1];
        names[0] = "-1";

        boolean doing_preferences = false;

        for (String line : parsedLines) {
            if (line.equals("")) {
                doing_preferences = true;
                continue;
            }
            if (!doing_preferences) {
                String[] tokens = line.split(" ");
                int id = Integer.valueOf(tokens[0]);
                String name = tokens[1];
                names[id] = name;
            } else {
                String[] tokens = line.split(":");
                int id = Integer.valueOf(tokens[0]);
                String[] preference_tokens = tokens[1].split(" ");
                List<Integer> current_preferences = new ArrayList<Integer>();
                for (String preference : preference_tokens) {
                    if (preference.equals("")) {
                        continue;
                    }
                    current_preferences.add(Integer.valueOf(preference.trim()));
                }
            }
        }
        for (String name : names) {
            System.out.println(name);
        }
    }
}
