package com.example.natan.appnutrientes;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class NecessidadeDetalhadasActivity extends AppCompatActivity {

    String nome;
    double caloriasTotais;
    TextView viewnome, proteinas, carboidratos, gorduras;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_necessidade_detalhadas);

        final Intent intent = getIntent();
        nome = intent.getStringExtra("Nome");
        caloriasTotais = intent.getDoubleExtra("CaloriasTotais", 0);
        viewnome = (TextView) findViewById(R.id.Nome);
        proteinas = (TextView) findViewById(R.id.proteina);
        carboidratos = (TextView) findViewById(R.id.carboidratos);
        gorduras = (TextView) findViewById(R.id.gorduras);

        viewnome.setText(String.format("Calorias detalhadas de %s", nome));
        Double caloriasProteinas = caloriasTotais * 0.15;
        proteinas.setText(String.format("Proteínas %.2f calorias(%.2f gramas)", caloriasProteinas, caloriasProteinas / 4));
        Double caloriasCarboidratos = caloriasTotais * 0.60;
        carboidratos.setText(String.format("Carboidratos %.2f calorias(%.2f gramas)", caloriasCarboidratos, caloriasCarboidratos / 4));
        Double caloriasGorduras = caloriasTotais * 0.25;
        gorduras.setText(String.format("Gorduras %.2f calorias(%.2f gramas)", caloriasGorduras, caloriasGorduras / 9));
    }

    public void voltar(View view) {
        finish();
    }
}
