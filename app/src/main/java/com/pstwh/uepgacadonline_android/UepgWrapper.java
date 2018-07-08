package com.pstwh.uepgacadonline_android;

import com.pstwh.uepgacadonline_android.models.Grade;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

/**
 * Created by pstwh on 06/07/2018.
 */

public class UepgWrapper implements Serializable {

    private Map<String, String> cookies;

    public UepgWrapper(final String login, final String password) {
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

    public ArrayList<Grade> getGrade()
            throws InterruptedException, ExecutionException {

        ExecutorService ex = Executors.newSingleThreadExecutor();
        Future<ArrayList<Grade>> future =
                ex.submit(new Callable<ArrayList<Grade>>() {
            public ArrayList<Grade> call() throws Exception {

                Document doc = Jsoup
                        .connect("https://sistemas.uepg.br/academicoonline/avaliacaoDesempenho/index")
                        .cookies(cookies)
                        .post();

                Element table = doc.select("table").get(0);
                Elements headers = table.select("th");
                Elements rows = table.select("tr");
                rows.remove(0);

                ArrayList<Grade> grades = new ArrayList<Grade>();

                for (int i = 0; i < rows.size(); i++) {
                    Elements cols = rows.get(i).select("td");
                    Grade grade = new Grade(
                            cols.get(0).text(),
                            cols.get(1).text(),
                            cols.get(2).text(),
                            cols.get(3).text(),
                            cols.get(4).text(),
                            cols.get(5).text(),
                            cols.get(6).text(),
                            cols.get(7).text(),
                            cols.get(8).text(),
                            cols.get(9).text(),
                            cols.get(10).text()
                    );

                    grades.add(grade);
                }

                return grades;
            }
        });

        ArrayList<Grade> grades = future.get();
        ex.shutdown();

        return grades;
    }


    public Map<String, String> getCookies() {
        return cookies;
    }
}
