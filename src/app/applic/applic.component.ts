import { Component, OnInit } from '@angular/core';
import { categories } from './categories';

@Component({
  selector: 'app-applic',
  templateUrl: './applic.component.html',
  styleUrls: ['./applic.component.css']
})
export class ApplicComponent implements OnInit {
  categories = categories;
  visible: boolean;
  constructor() {
    this.visible = false;
  }

  ngOnInit(): void {
  }
  categorySelection(id: number): void
  {
     this.visible = !this.visible;
  }

}
