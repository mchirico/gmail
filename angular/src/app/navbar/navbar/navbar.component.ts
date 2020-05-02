import {Component, OnInit, ViewChild} from '@angular/core';
import {NgForm} from '@angular/forms';
import {SearchService} from '../../service/search.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  @ViewChild('f') searchForm: NgForm;

  constructor(private searchService: SearchService) {
  }

  ngOnInit(): void {
  }

  onSubmit() {
    console.log('Native val: ', this.searchForm.value.search0)
    this.searchService.putTerm(this.searchForm.value.search0);
    console.log('results: ', this.searchService.getTerms());
  }
}
