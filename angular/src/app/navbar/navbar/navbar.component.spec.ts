import {async, ComponentFixture, TestBed} from '@angular/core/testing';
import {FormBuilder, FormsModule} from '@angular/forms';
import {NavbarComponent} from './navbar.component';
import {BrowserModule} from '@angular/platform-browser';
import {AppRoutingModule} from '../../app-routing.module';
import {DebugElement} from '@angular/core';
import {SearchService} from '../../service/search.service';


describe('NavbarComponent', () => {
  let component: NavbarComponent;
  let fixture: ComponentFixture<NavbarComponent>;

  let getQuoteSpy;
  let searchServiceResult;

  beforeEach(async(() => {

    const searchServiceStub = jasmine.createSpyObj('SearchService', ['putTerm', 'getTerms']);

    getQuoteSpy = searchServiceStub.getTerms.and.returnValue(['one']);

    TestBed.configureTestingModule({
      declarations: [NavbarComponent],
      providers: [{provide: SearchService, useValue: searchServiceStub}],
      imports: [
        BrowserModule,
        FormsModule,
        AppRoutingModule
      ],
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NavbarComponent);
    component = fixture.componentInstance;
    // from the root injector

    searchServiceResult = TestBed.inject(SearchService);
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  it('should call service onSubmit', () => {

    const myModel = {
      search0: 'sample data'
    };
    const fb = new FormBuilder();
    const form = fb.group(myModel);
    component.searchForm.form = form;
    fixture.detectChanges();

    component.onSubmit();
    expect(searchServiceResult.putTerm.calls.count()).toBeGreaterThan(0);
    expect(searchServiceResult.getTerms.calls.count()).toBeGreaterThan(0);

  });


});
