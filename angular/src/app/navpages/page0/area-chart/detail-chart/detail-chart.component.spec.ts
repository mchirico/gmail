import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailChartComponent } from './detail-chart.component';

describe('DetailChartComponent', () => {
  let component: DetailChartComponent;
  let fixture: ComponentFixture<DetailChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DetailChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DetailChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
