import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ApplicComponent } from './applic.component';

describe('AppComponent', () => {
  let component: ApplicComponent;
  let fixture: ComponentFixture<ApplicComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ApplicComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ApplicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
