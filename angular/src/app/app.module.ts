import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AuthComponent } from './navpages/auth/auth.component';
import { Page0Component } from './navpages/page0/page0.component';
import { Page1Component } from './navpages/page1/page1.component';
import { MainComponent } from './navpages/main/main.component';
import { SearchComponent } from './navpages/search/search.component';
import { NavbarComponent } from './navbar/navbar/navbar.component';
import { AreaChartComponent } from './navpages/page0/area-chart/area-chart.component';
import { StartChartComponent } from './navpages/page0/area-chart/start-chart/start-chart.component';
import { DetailChartComponent } from './navpages/page0/area-chart/detail-chart/detail-chart.component';
import { HomeComponent } from './navpages/home/home.component';
import {FormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    AuthComponent,
    Page0Component,
    Page1Component,
    MainComponent,
    SearchComponent,
    NavbarComponent,
    AreaChartComponent,
    StartChartComponent,
    DetailChartComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
