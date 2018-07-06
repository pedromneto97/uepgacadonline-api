package com.pstwh.uepgacadonline_android;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by pstwh on 06/07/2018.
 */

public class Scrapper {

    private Map<String, String> cookies;

    public Scrapper(final String login, final String password) {
        Thread t = new Thread(new Runnable() {
            @Override
            public void run() {
                try {

                    Connection.Response res = Jsoup
                            .connect("https://sistemas.uepg.br/academicoonline/login/index")
                            .method(Connection.Method.GET)
                            .followRedirects(false)
                            .execute();

                    cookies = res.cookies();

                    Document doc = Jsoup
                            .connect("https://sistemas.uepg.br/academicoonline/login/authenticate")
                            .cookies(cookies)
                            .data("login", login)
                            .data("password", password)
                            .post();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });

        t.start();
        try {
            t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void getGrade() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Document doc = Jsoup
                            .connect("https://sistemas.uepg.br/academicoonline/avaliacaoDesempenho/index")
                            .cookies(cookies)
                            .post();

                    Element table = doc.select("table").get(0);
                    Elements headers = table.select("th");
                    Elements rows = table.select("tr");
                    rows.remove(0);

                    ArrayList<ArrayList<HashMap<String, String>>> grades =
                            new ArrayList<ArrayList<HashMap<String, String>>>();

                    for (int i = 0; i < rows.size(); i++) {

                        ArrayList<HashMap<String, String>> grade =
                                new ArrayList<HashMap<String, String>>();

                        Elements colsElement = rows.get(i).select("td");
                        for (int j = 0; j < colsElement.size(); j++) {
                            HashMap<String, String> aux = new HashMap<String, String>();
                            aux.put(headers.get(j).text(), colsElement.get(j).text());
                            grade.add(aux);
                        }
                        grades.add(grade);
                    }

                    System.out.println(grades);
                } catch (IOException e) {
                    e.printStackTrace();
                }

            }
        }).start();
    }

    public Map<String, String> getCookies() {
        return cookies;
    }
}
