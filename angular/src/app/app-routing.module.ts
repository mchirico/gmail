import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AuthComponent} from './navpages/auth/auth.component';
import {HomeComponent} from './navpages/home/home.component';
import {MainComponent} from './navpages/main/main.component';

import {Page0Component} from './navpages/page0/page0.component';
import {AreaChartComponent} from './navpages/page0/area-chart/area-chart.component';

import {Page1Component} from './navpages/page1/page1.component';
import {SearchComponent} from './navpages/search/search.component';

const routes: Routes = [
  {path: '', redirectTo: '/main', pathMatch: 'full'},
  {path: 'home', component: HomeComponent},
  {path: 'main', component: MainComponent},
  {
    path: 'page0', component: Page0Component, children: [
      {path: '', component: AreaChartComponent},
    ]
  },
  {path: 'page1', component: Page1Component},
  {path: 'auth', component: AuthComponent},
  {path: 'search', component: SearchComponent}

];



@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
